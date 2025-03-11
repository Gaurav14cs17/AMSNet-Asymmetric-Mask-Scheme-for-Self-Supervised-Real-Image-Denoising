# Learning Enriched Features for Real Image Restoration and Enhancement  

[![Paper](https://img.shields.io/badge/arXiv-2003.06792-b31b1b.svg)](https://arxiv.org/pdf/2003.06792)  

This repository contains the implementation of **Learning Enriched Features for Real Image Restoration and Enhancement**, where we propose a deep learning framework to enhance real-world images affected by noise and degradation.  

## Overview  

Real-world images often suffer from complex degradations, including noise, blur, and artifacts. Our method introduces a **multi-scale feature enrichment module** that enhances representational capability for better restoration. Our approach is validated on multiple real-image denoising benchmarks, achieving state-of-the-art results.  

## Benchmark Results  

### Denoising on SIDD Dataset  

| Method  | DnCNN | MLP | GLIDE | TNRD | FoE | BM3D | WNNM | NLM | KSVD | EPLL | CBDNet | RIDNet | VDN | **MIRNet (Ours)** |
|---------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|----------------|
| **PSNR ↑**  | 23.66 | 24.71 | 24.71 | 24.73 | 25.58 | 25.65 | 25.78 | 26.76 | 26.88 | 27.11 | 30.78 | 38.71 | 39.28 | **39.72** |
| **SSIM ↑**  | 0.583 | 0.641 | 0.774 | 0.643 | 0.792 | 0.685 | 0.809 | 0.699 | 0.842 | 0.870 | 0.754 | 0.914 | 0.909 | **0.959** |

### Denoising on DND Dataset  

| Method  | EPLL | TNRD | MLP | BM3D | FoE | WNNM | KSVD | MCWNNM | FFDNet+ | TWSC | CBDNet | RIDNet | VDN | **MIRNet (Ours)** |
|---------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|----------------|
| **PSNR ↑**  | 33.51 | 33.65 | 34.23 | 34.51 | 34.62 | 34.67 | 36.49 | 37.38 | 37.61 | 37.94 | 38.06 | 39.26 | 39.38 | **39.88** |
| **SSIM ↑**  | 0.824 | 0.831 | 0.833 | 0.851 | 0.885 | 0.865 | 0.898 | 0.929 | 0.942 | 0.940 | 0.942 | 0.953 | 0.952 | **0.956** |

## Paper  

For more details, check out our paper:  
📄 **[Learning Enriched Features for Real Image Restoration and Enhancement (arXiv)](https://arxiv.org/pdf/2003.06792)**  

---
