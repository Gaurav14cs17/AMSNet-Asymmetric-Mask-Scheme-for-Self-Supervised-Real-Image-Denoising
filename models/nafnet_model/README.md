# Simple Baselines for Image Restoration  

[![Paper](https://img.shields.io/badge/arXiv-2204.04676-b31b1b.svg)](https://arxiv.org/pdf/2204.04676)  

## Overview  
This repository provides an implementation of simple yet effective baselines for image restoration tasks. Our approach achieves state-of-the-art performance while maintaining lower computational cost compared to existing methods.  

## Benchmark Comparison  

| Method   | MPRNet [37] | MIRNet [40] | NBNet [6] | UFormer [36] | MAXIM [32] | HINet [5] | Restormer [39] | Baseline (Ours) | NAFNet (Ours) |
|----------|------------|-------------|-----------|--------------|------------|------------|---------------|----------------|--------------|
| **PSNR** | 39.71      | 39.72       | 39.75     | 39.89        | 39.96      | 39.99      | 40.02         | 40.30          | 40.30        |
| **SSIM** | 0.958      | 0.959       | 0.959     | 0.960        | 0.960      | 0.958      | 0.960         | 0.962          | 0.962        |
| **MACs(G)** | 588  | 786         | 88.8      | 89.5         | 169.5      | 170.7      | 140           | 84             | 65           |

## Raw Image Denoising  
We apply NAFNet to a raw image denoising task following PMRID [35]. The testing set, referred to as **4Scenes**, consists of 39 raw images captured in different lighting conditions. To ensure a fair comparison, we adjusted NAFNet's width and the number of blocks from 32 to 16 and 36 to 7, respectively, reducing computational cost below PMRID.  


