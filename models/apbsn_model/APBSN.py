
from einops import rearrange
import torch
import torch.nn as nn
import torch.nn.functional as F

from codes.util.util import pixel_shuffle_down_sampling, pixel_shuffle_up_sampling
import torch
import torch.nn as nn
import torch.nn.functional as F
import numbers

from codes.model.Unet import UNet
##########################################################################


class DBSNl(nn.Module):
    '''
    Dilated Blind-Spot Network (cutomized light version)

    self-implemented version of the network from "Unpaired Learning of Deep Image Denoising (ECCV 2020)"
    and several modificaions are included. 
    see our supple for more details. 
    '''

    def __init__(self, in_ch=3, out_ch=3, base_ch=128, num_module=9):
        '''
        Args:
            in_ch      : number of input channel
            out_ch     : number of output channel
            base_ch    : number of base channel
            num_module : number of modules in the network
        '''
        super().__init__()

        assert base_ch % 2 == 0, "base channel should be divided with 2"

        ly = []
        ly += [nn.Conv2d(in_ch, base_ch, kernel_size=1)]
        ly += [nn.ReLU(inplace=True)]
        self.head = nn.Sequential(*ly)

        self.branch1 = DC_branchl(2, base_ch, num_module)
        self.branch2 = DC_branchl(3, base_ch, num_module)

        ly = []
        ly += [nn.Conv2d(base_ch*2,  base_ch,    kernel_size=1)]
        ly += [nn.ReLU(inplace=True)]
        ly += [nn.Conv2d(base_ch,    base_ch//2, kernel_size=1)]
        ly += [nn.ReLU(inplace=True)]
        ly += [nn.Conv2d(base_ch//2, base_ch//2, kernel_size=1)]
        ly += [nn.ReLU(inplace=True)]
        ly += [nn.Conv2d(base_ch//2, out_ch,     kernel_size=1)]
        self.tail = nn.Sequential(*ly)

    def forward(self, x):
        x = self.head(x)

        br1 = self.branch1(x)
        br2 = self.branch2(x)

        x = torch.cat([br1, br2], dim=1)

        return self.tail(x)

    def _initialize_weights(self):
        # Liyong version
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                # n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, (2 / (9.0 * 64)) ** 0.5)


class DC_branchl(nn.Module):
    def __init__(self, stride, in_ch, num_module):
        super().__init__()

        ly = []
        ly += [CentralMaskedConv2d(in_ch, in_ch, kernel_size=2 *
                                   stride-1, stride=1, padding=stride-1)]
        ly += [nn.ReLU(inplace=True)]
        ly += [nn.Conv2d(in_ch, in_ch, kernel_size=1)]
        ly += [nn.ReLU(inplace=True)]
        ly += [nn.Conv2d(in_ch, in_ch, kernel_size=1)]
        ly += [nn.ReLU(inplace=True)]

        ly += [DCl(stride, in_ch) for _ in range(num_module)]

        ly += [nn.Conv2d(in_ch, in_ch, kernel_size=1)]
        ly += [nn.ReLU(inplace=True)]

        self.body = nn.Sequential(*ly)

    def forward(self, x):
        return self.body(x)


class DCl(nn.Module):
    def __init__(self, stride, in_ch):
        super().__init__()

        ly = []
        ly += [nn.Conv2d(in_ch, in_ch, kernel_size=3, stride=1,
                         padding=stride, dilation=stride)]
        ly += [nn.ReLU(inplace=True)]
        ly += [nn.Conv2d(in_ch, in_ch, kernel_size=1)]
        self.body = nn.Sequential(*ly)

    def forward(self, x):
        return x + self.body(x)


class CentralMaskedConv2d(nn.Conv2d):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.register_buffer('mask', self.weight.data.clone())
        _, _, kH, kW = self.weight.size()
        self.mask.fill_(1)
        self.mask[:, :, kH//2, kH//2] = 0

    def forward(self, x):
        self.weight.data *= self.mask
        return super().forward(x)

class DBSNlWU(nn.Module):
    '''
    Dilated Blind-Spot Network with unet 

    self-implemented version of the network from "Unpaired Learning of Deep Image Denoising (ECCV 2020)"
    and several modificaions are included. 
    see our supple for more details. 
    '''

    def __init__(self, in_ch=3, out_ch=3, base_ch=128, num_module=9):
        '''
        Args:
            in_ch      : number of input channel
            out_ch     : number of output channel
            base_ch    : number of base channel
            num_module : number of modules in the network
        '''
        super().__init__()

        assert base_ch % 2 == 0, "base channel should be divided with 2"

        ly = []
        ly += [UNet(in_ch,base_ch,base_ch)]
        self.head = nn.Sequential(*ly)

        self.branch1 = DC_branchl(2, base_ch, num_module)
        self.branch2 = DC_branchl(3, base_ch, num_module)

        ly = [UNet(in_ch,base_ch,base_ch)]
        self.tail = nn.Sequential(*ly)

    def forward(self, x):
        x = self.head(x)

        br1 = self.branch1(x)
        br2 = self.branch2(x)

        x = torch.cat([br1, br2], dim=1)

        return self.tail(x)

    def _initialize_weights(self):
        # Liyong version
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                # n = m.kernel_size[0] * m.kernel_size[1] * m.out_channels
                m.weight.data.normal_(0, (2 / (9.0 * 64)) ** 0.5)

class APBSNORI(nn.Module):
    '''
    Asymmetric PD Blind-Spot Network (AP-BSN)
    '''

    def __init__(self, pd_a=5, pd_b=2, pd_pad=2, R3=True, R3_T=8, R3_p=0.16,
                 bsn='DBSNl', in_ch=3, bsn_base_ch=128, bsn_num_module=9):
        '''
        Args:
            pd_a           : 'PD stride factor' during training
            pd_b           : 'PD stride factor' during inference
            pd_pad         : pad size between sub-images by PD process
            R3             : flag of 'Random Replacing Refinement'
            R3_T           : number of masks for R3
            R3_p           : probability of R3
            bsn            : blind-spot network type
            in_ch          : number of input image channel
            bsn_base_ch    : number of bsn base channel
            bsn_num_module : number of module
        '''
        super().__init__()

        # network hyper-parameters
        self.pd_a = pd_a
        self.pd_b = pd_b
        self.pd_pad = pd_pad
        self.R3 = R3
        self.R3_T = R3_T
        self.R3_p = R3_p

        # define network
        if bsn == 'DBSNl':
            self.bsn = DBSNl(in_ch, in_ch, bsn_base_ch, bsn_num_module)
        else:
            raise NotImplementedError('bsn %s is not implemented' % bsn)

    def forward(self, img, pd=None):
        '''
        Foward function includes sequence of PD, BSN and inverse PD processes.
        Note that denoise() function is used during inference time (for differenct pd factor and R3).
        '''
        # default pd factor is training factor (a)
        if pd is None:
            pd = self.pd_a

        # do PD
        if pd > 1:
            pd_img = pixel_shuffle_down_sampling(img, f=pd, pad=self.pd_pad)
        else:
            p = self.pd_pad
            pd_img = F.pad(img, (p, p, p, p))

        # forward blind-spot network
        pd_img_denoised = self.bsn(pd_img)

        # do inverse PD
        if pd > 1:
            img_pd_bsn = pixel_shuffle_up_sampling(
                pd_img_denoised, f=pd, pad=self.pd_pad)
        else:
            p = self.pd_pad
            img_pd_bsn = pd_img_denoised[:, :, p:-p, p:-p]

        return img_pd_bsn

    def denoise(self, x):
        '''
        Denoising process for inference.
        '''
        b, c, h, w = x.shape

        # pad images for PD process
        if h % self.pd_b != 0:
            x = F.pad(x, (0, 0, 0, self.pd_b - h %
                      self.pd_b), mode='constant', value=0)
        if w % self.pd_b != 0:
            x = F.pad(x, (0, self.pd_b - w % self.pd_b, 0, 0),
                      mode='constant', value=0)

        # forward PD-BSN process with inference pd factor
        img_pd_bsn = self.forward(img=x, pd=self.pd_b)

        # Random Replacing Refinement
        if not self.R3:
            ''' Directly return the result (w/o R3) '''
            return img_pd_bsn[:, :, :h, :w]
        else:
            denoised = torch.empty(*(x.shape), self.R3_T, device=x.device)
            for t in range(self.R3_T):
                indice = torch.rand_like(x)
                mask = indice < self.R3_p

                tmp_input = torch.clone(img_pd_bsn).detach()
                tmp_input[mask] = x[mask]
                p = self.pd_pad
                tmp_input = F.pad(tmp_input, (p, p, p, p), mode='reflect')
                if self.pd_pad == 0:
                    denoised[..., t] = self.bsn(tmp_input)
                else:
                    denoised[..., t] = self.bsn(tmp_input)[:, :, p:-p, p:-p]

            return torch.mean(denoised, dim=-1)

        '''
        elif self.R3 == 'PD-refinement':
            s = 2
            denoised = torch.empty(*(x.shape), s**2, device=x.device)
            for i in range(s):
                for j in range(s):
                    tmp_input = torch.clone(x_mean).detach()
                    tmp_input[:,:,i::s,j::s] = x[:,:,i::s,j::s]
                    p = self.pd_pad
                    tmp_input = F.pad(tmp_input, (p,p,p,p), mode='reflect')
                    if self.pd_pad == 0:
                        denoised[..., i*s+j] = self.bsn(tmp_input)
                    else:
                        denoised[..., i*s+j] = self.bsn(tmp_input)[:,:,p:-p,p:-p]
            return_denoised = torch.mean(denoised, dim=-1)
        else:
            raise RuntimeError('post-processing type not supported')
        '''
