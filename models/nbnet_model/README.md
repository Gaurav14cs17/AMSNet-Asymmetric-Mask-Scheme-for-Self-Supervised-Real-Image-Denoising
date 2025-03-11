# Simple Baselines for Image Restoration  

This repository provides simple yet effective baselines for image restoration. The methods are evaluated on standard datasets for image denoising, demonstrating competitive performance compared to existing approaches.

## 📜 Paper  

[NBNet: Noise Basis Learning for Image Denoising with Subspace Projection (CVPR 2021)](https://openaccess.thecvf.com/content/CVPR2021/papers/Cheng_NBNet_Noise_Basis_Learning_for_Image_Denoising_With_Subspace_Projection_CVPR_2021_paper.pdf)

## 📊 Benchmark Results  

The following table presents the PSNR (Peak Signal-to-Noise Ratio) results for various methods on standard datasets with different noise levels (σ = 15, 25, 50).  

| Cases | Datasets | CBM3D [39] | WNNM [19] | NCSR [16] | MLP [10] | DnCNN-B [50] | MemNet [40] | FFDNet [52] | FFDNetv [52] | UDNet [24] | VDN [47] | **Ours** |
|-------|----------|------------|------------|------------|------------|----------------|--------------|--------------|--------------|------------|------------|------------|
| **σ = 15** | **Set5** | 33.42 | 32.92 | 32.57 | - | 34.04 | 34.18 | 34.30 | 34.31 | 34.19 | 34.34 | **34.64** |
|  | **LIVE1** | 32.85 | 31.70 | 31.46 | - | 33.72 | 33.84 | 33.96 | 33.96 | 33.74 | 33.94 | **34.25** |
|  | **BSD68** | 32.67 | 31.27 | 30.84 | - | 33.87 | 33.76 | 33.85 | 33.68 | 33.76 | 33.90 | **34.15** |
| **σ = 25** | **Set5** | 30.92 | 30.61 | 30.33 | 30.55 | 31.88 | 31.98 | 32.10 | 32.09 | 31.82 | 32.24 | **32.51** |
|  | **LIVE1** | 30.05 | 29.15 | 29.05 | 29.16 | 31.23 | 31.26 | 31.37 | 31.37 | 31.09 | 31.50 | **31.73** |
|  | **BSD68** | 29.83 | 28.62 | 28.35 | 28.93 | 31.22 | 31.17 | 31.21 | 31.20 | 31.02 | 31.35 | **31.54** |
| **σ = 50** | **Set5** | 28.16 | 27.58 | 27.20 | 27.59 | 28.95 | 29.10 | 29.25 | 29.25 | 28.87 | 29.47 | **29.70** |
|  | **LIVE1** | 26.98 | 26.07 | 26.06 | 26.12 | 27.95 | 27.99 | 28.10 | 28.10 | 27.82 | 28.36 | **28.55** |
|  | **BSD68** | 26.81 | 25.86 | 25.75 | 26.01 | 27.91 | 27.91 | 27.95 | 27.95 | 27.76 | 28.19 | **28.35** |

---  
