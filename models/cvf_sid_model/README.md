# **Real-World sRGB Image Denoising**

This repository focuses on **real-world sRGB image denoising**, evaluating various methods on the **SIDD (Smartphone Image Denoising Dataset)** and **DND (Darmstadt Noise Dataset)** benchmarks. The results are compared in terms of **PSNR (Peak Signal-to-Noise Ratio)** and **SSIM (Structural Similarity Index Measure)**.

---

## **Results**

### **Table 1: Quantitative Comparison of Real-World sRGB Image Denoising**
The table below compares different denoising methods on the **SIDD** and **DND** datasets.

| Type of Supervision | Training Data          | Method               | SIDD PSNR | SIDD SSIM | DND PSNR | DND SSIM |
|---------------------|------------------------|----------------------|-----------|-----------|----------|----------|
| **Supervised**      | Paired noisy/clean     |                      |           |           |          |          |
|                     |                        | MLP [6]              | 24.71     | 0.641     | 34.23    | 0.833    |
|                     |                        | TNRD [8]             | 24.73     | 0.643     | 33.65    | 0.830    |
|                     |                        | DnCNN [33]           | 23.66     | 0.583     | 32.43    | 0.790    |
|                     |                        | DnCNN+ [33]          | 32.59     | 0.861     | 37.90    | 0.943    |
|                     |                        | CBDNet [12]          | 33.28     | 0.868     | 38.05    | 0.942    |
|                     |                        | RIDNet [3]           | 38.70     | 0.950     | 39.25    | 0.952    |
|                     |                        | DIDN [32]            | 39.82     | 0.973     | 39.62    | 0.954    |
| **Unsupervised**    | Unpaired noisy/clean   |                      |           |           |          |          |
|                     |                        | GCBD [7]             | -         | -         | 35.58    | 0.922    |
|                     |                        | UIDNet [13]          | 32.48     | 0.897     | -        | -        |
|                     |                        | C2N [16]             | 35.35     | 0.937     | 36.38    | 0.887    |
|                     | Paired noisy/noisy     | R2R [25]             | 34.78     | 0.844     | -        | -        |
| **Self-supervised** | Paired noisy/noisy     |                      |           |           |          |          |
|                     |                        | N2V [18]             | 27.68     | 0.668     | -        | -        |
|                     |                        | N2S [4]              | 29.56     | 0.808     | -        | -        |
|                     |                        | NAC [30]             | -         | -         | 36.20    | 0.925    |
|                     | Single noisy           |                      |           |           |          |          |
|                     |                        | CVF-SID (T) (Ours)   | 34.43     | 0.912     | 36.31    | 0.923    |
|                     |                        | CVF-SID (S) (Ours)   | 34.51     | 0.916     | 36.49    | 0.924    |
|                     |                        | CVF-SID (S²) (Ours)  | 34.71     | 0.917     | 36.50    | 0.924    |

---

### **Key Observations**
1. **Supervised Methods**:
   - **DIDN [32]** achieves the best performance on both SIDD (PSNR = 39.82, SSIM = 0.973) and DND (PSNR = 39.62, SSIM = 0.954).
   - **RIDNet [3]** and **CBDNet [12]** also perform well, demonstrating the effectiveness of supervised learning with paired noisy/clean data.

2. **Unsupervised Methods**:
   - **C2N [16]** performs well on SIDD (PSNR = 35.35, SSIM = 0.937) and DND (PSNR = 36.38, SSIM = 0.887).
   - **GCBD [7]** and **UIDNet [13]** show competitive results but are limited to specific datasets.

3. **Self-supervised Methods**:
   - **N2V [18]** and **N2S [4]** perform moderately on SIDD but lack results on DND.
   - **NAC [30]** achieves good results on DND (PSNR = 36.20, SSIM = 0.925).

4. **Proposed Method (CVF-SID)**:
   - **CVF-SID (T)**: PSNR = 34.43 (SIDD), 36.31 (DND); SSIM = 0.912 (SIDD), 0.923 (DND).
   - **CVF-SID (S)**: PSNR = 34.51 (SIDD), 36.49 (DND); SSIM = 0.916 (SIDD), 0.924 (DND).
   - **CVF-SID (S²)**: PSNR = 34.71 (SIDD), 36.50 (DND); SSIM = 0.917 (SIDD), 0.924 (DND).
   - The proposed method achieves competitive results, especially considering it uses only single noisy images for training.

---

## **Paper Link**
The paper associated with this work can be accessed here:  
[**CVF-SID: Real-World Denoising via Self-Supervised Learning**](https://arxiv.org/pdf/2203.13009)

---
