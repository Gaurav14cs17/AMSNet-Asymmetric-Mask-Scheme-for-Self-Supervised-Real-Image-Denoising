

# Restormer: Efficient Transformer for High-Resolution Image Restoration  

[![Paper](https://img.shields.io/badge/arXiv-2111.09881-b31b1b.svg)](https://arxiv.org/abs/2111.09881)  

## Introduction  

Restormer is a novel Transformer-based network for image restoration tasks such as denoising, deraining, and deblurring. Unlike convolution-based methods, Restormer efficiently models global contextual information using self-attention while maintaining computational efficiency.  

## Gaussian Image Denoising Results  

Restormer achieves **state-of-the-art** performance in **Gaussian grayscale and color image denoising** compared to prior CNN-based and Transformer-based methods.  

### Grayscale Image Denoising (PSNR in dB)  

| Method   | Set12 (σ=15) | Set12 (σ=25) | Set12 (σ=50) | BSD68 (σ=15) | BSD68 (σ=25) | BSD68 (σ=50) | Urban100 (σ=15) | Urban100 (σ=25) | Urban100 (σ=50) |
|----------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| DnCNN   | 32.67 | 30.35 | 27.18 | 31.62 | 29.16 | 26.23 | 32.28 | 29.80 | 26.35 |
| FFDNet  | 32.75 | 30.43 | 27.32 | 31.63 | 29.19 | 26.29 | 32.40 | 29.90 | 26.50 |
| DRUNet  | 33.25 | 30.94 | 27.90 | 31.91 | 29.48 | 26.59 | 33.44 | 31.11 | 27.96 |
| **Restormer** | **33.42** | **31.08** | **28.00** | **31.96** | **29.52** | **26.62** | **33.79** | **31.46** | **28.29** |

### Color Image Denoising (PSNR in dB)  

| Method   | CBSD68 (σ=15) | CBSD68 (σ=25) | CBSD68 (σ=50) | Kodak24 (σ=15) | Kodak24 (σ=25) | Kodak24 (σ=50) | McMaster (σ=15) | McMaster (σ=25) | McMaster (σ=50) | Urban100 (σ=15) | Urban100 (σ=25) | Urban100 (σ=50) |
|----------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| IRCNN   | 33.86 | 31.16 | 27.86 | 34.69 | 32.18 | 28.93 | 34.58 | 32.18 | 28.91 | 33.78 | 31.20 | 27.70 |
| FFDNet  | 33.87 | 31.21 | 27.96 | 34.63 | 32.13 | 28.98 | 34.66 | 32.35 | 29.18 | 33.83 | 31.40 | 28.05 |
| DRUNet  | 34.30 | 31.69 | 28.51 | 35.31 | 32.89 | 29.86 | 35.40 | 33.14 | 30.08 | 34.81 | 32.60 | 29.61 |
| **Restormer** | **34.40** | **31.79** | **28.60** | **35.47** | **33.04** | **30.01** | **35.61** | **33.34** | **30.30** | **35.13** | **32.96** | **30.02** |

Restormer outperforms prior methods, offering better denoising capability, especially in **high-noise scenarios (σ=50)**.  

For more details, refer to our [paper](https://arxiv.org/abs/2111.09881).
