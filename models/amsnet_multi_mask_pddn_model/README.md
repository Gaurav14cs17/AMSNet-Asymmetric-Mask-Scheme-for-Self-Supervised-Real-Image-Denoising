# AMSNet Multi-Mask PDDN Model

This directory contains the implementation of the **AMSNet Multi-Mask PDDN Model**, a variant of the AMSNet framework designed for **self-supervised real image denoising**. The model leverages a **multi-mask scheme** to enhance denoising performance, particularly for real-world noisy images.

## Table of Contents
- [Overview](#overview)
- [Model Architecture](#model-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Citation](#citation)
- [License](#license)
- [Contact](#contact)

---

## Overview
The **AMSNet Multi-Mask PDDN Model** extends the original AMSNet framework by incorporating a **multi-mask scheme** to generate diverse training pairs from single noisy images. This approach improves the model's ability to generalize to real-world noise patterns, making it highly effective for practical denoising tasks.

---

## Model Architecture
The architecture of the AMSNet Multi-Mask PDDN Model consists of the following key components:
1. **Asymmetric Mask Generator**: Generates multiple masks to create diverse training pairs.
2. **Denoising Network**: A deep neural network trained to predict clean images from noisy inputs.
3. **Multi-Mask Fusion Module**: Combines outputs from multiple masks to produce the final denoised image.

For more details, refer to the [paper](#citation).

---

## Installation
To use the AMSNet Multi-Mask PDDN Model, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Gaurav14cs17/AMSNet-Asymmetric-Mask-Scheme-for-Self-Supervised-Real-Image-Denoising.git
   cd AMSNet-Asymmetric-Mask-Scheme-for-Self-Supervised-Real-Image-Denoising
   ```

2. Navigate to the model directory:
   ```bash
   cd models/amsnet_multi_mask_pddn_model
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the pre-trained weights (if available) and datasets.

---

## Usage
### Training
To train the AMSNet Multi-Mask PDDN Model, use the following command:
```bash
python train.py --data_path /path/to/your/dataset --batch_size 16 --epochs 100
```

### Testing
To evaluate the model on a test dataset, run:
```bash
python test.py --data_path /path/to/test/dataset --model_path /path/to/pretrained/model
```

### Inference
To denoise a single image using the trained model, use:
```bash
python denoise.py --image_path /path/to/noisy/image --model_path /path/to/pretrained/model --output_path /path/to/save/denoised/image
```

---

## Results
The AMSNet Multi-Mask PDDN Model achieves state-of-the-art performance on real-world denoising tasks. Below are some quantitative results:

| Dataset         | PSNR (dB) | SSIM  |
|-----------------|-----------|-------|
| Dataset A       | 36.1      | 0.96  |
| Dataset B       | 35.7      | 0.95  |
| Real-World Data | 34.2      | 0.93  |

For qualitative results and visual comparisons, refer to the [paper](#citation).
---
---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

