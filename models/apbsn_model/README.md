
---
### **Key Observations from the Table**
1. **Non-learning-based Methods**:
   - **BM3D [9]**: PSNR = 25.65 (SIDD), 34.51 (DND); SSIM = 0.685 (SIDD), 0.851 (DND).
   - **WNNM [12]**: PSNR = 25.78 (SIDD), 34.67 (DND); SSIM = 0.809 (SIDD), 0.865 (DND).
   - These methods are traditional and do not rely on learning from data.

2. **Supervised Methods (Synthetic Pairs)**:
   - **DnCNN [44]**: PSNR = 23.66 (SIDD), 32.43 (DND); SSIM = 0.583 (SIDD), 0.790 (DND).
   - **CBDNet [13]**: PSNR = 33.28 (SIDD), 38.05 (DND); SSIM = 0.868 (SIDD), 0.942 (DND).
   - **Zhou et al. [46]**: PSNR = 34.00 (SIDD), 38.40 (DND); SSIM = 0.898 (SIDD), 0.945 (DND).
   - These methods use synthetic noisy-clean pairs for training.

3. **Supervised Methods (Real Pairs)**:
   - **DnCNN [44]**: PSNR = 35.13 (SIDD), 37.89 (DND); SSIM = 0.896 (SIDD), 0.932 (DND).
   - **AINDNet (R)∗ [21]**: PSNR = 38.84 (SIDD), 39.34 (DND); SSIM = 0.951 (SIDD), 0.952 (DND).
   - **VDN [42]**: PSNR = 39.26 (SIDD), 39.38 (DND); SSIM = 0.955 (SIDD), 0.952 (DND).
   - **DANet [43]**: PSNR = 39.43 (SIDD), 39.58 (DND); SSIM = 0.956 (SIDD), 0.955 (DND).
   - These methods leverage real noisy-clean pairs for training and generally achieve the best performance.

4. **Unsupervised Methods (Unpaired)**:
   - **GCBD [7]**: PSNR = N/A (SIDD), 35.58 (DND); SSIM = N/A (SIDD), 0.922 (DND).
   - **C2N [19] + DIDN∗ [41]**: PSNR = 35.35 (SIDD), 37.28 (DND); SSIM = 0.937 (SIDD), 0.924 (DND).
   - **D-BSN [38] + MWCNN [28]**: PSNR = N/A (SIDD), 37.93 (DND); SSIM = N/A (SIDD), 0.937 (DND).
   - These methods do not require paired noisy-clean data for training.

5. **Self-supervised Methods**:
   - **Noise2Void [23]**: PSNR = 27.68 (SIDD), N/A (DND); SSIM = 0.668 (SIDD), N/A (DND).
   - **Noise2Self [3]**: PSNR = 29.56 (SIDD), N/A (DND); SSIM = 0.808 (SIDD), N/A (DND).
   - **NAC [40]**: PSNR = N/A (SIDD), 36.20 (DND); SSIM = N/A (SIDD), 0.925 (DND).
   - **R2R [32]**: PSNR = 34.78 (SIDD), N/A (DND); SSIM = 0.898 (SIDD), N/A (DND).
   - These methods use only noisy images for training.

6. **Proposed Method (AP-BSN)**:
   - **AP-BSN**: PSNR = 34.90 (SIDD), 37.46 (DND); SSIM = 0.900 (SIDD), 0.924 (DND).
   - **AP-BSN + R³**: PSNR = 35.97 (SIDD), 38.09 (DND); SSIM = 0.925 (SIDD), 0.937 (DND).
   - **AP-BSN† + R³**: PSNR = 36.91 (SIDD), N/A (DND); SSIM = 0.931 (SIDD), N/A (DND).
   - The proposed method is self-supervised and achieves competitive results compared to supervised methods.

---

### **Key Takeaways**
- **Supervised methods** (especially those using real noisy-clean pairs) generally outperform unsupervised and self-supervised methods.
- The proposed **AP-BSN** method achieves strong performance despite being self-supervised, demonstrating the effectiveness of the approach.
- The use of **self-ensemble strategy** (marked with ∗) and additional refinements (e.g., R³) further improves performance.

---

### **PSNR Table Format**
Here’s how the table can be formatted for clarity:

| Method                     | SIDD PSNR | SIDD SSIM | DND PSNR | DND SSIM |
|----------------------------|-----------|-----------|----------|----------|
| **Non-learning-based**     |           |           |          |          |
| BM3D [9]                   | 25.65     | 0.685     | 34.51    | 0.851    |
| WNNM [12]                  | 25.78     | 0.809     | 34.67    | 0.865    |
| **Supervised (Synthetic)** |           |           |          |          |
| DnCNN [44]                 | 23.66     | 0.583     | 32.43    | 0.790    |
| CBDNet [13]                | 33.28     | 0.868     | 38.05    | 0.942    |
| Zhou et al. [46]           | 34.00⋄    | 0.898⋄    | 38.40    | 0.945    |
| **Supervised (Real)**      |           |           |          |          |
| DnCNN [44]                 | 35.13⋄    | 0.896⋄    | 37.89⋄   | 0.932⋄   |
| AINDNet (R)∗ [21]          | 38.84     | 0.951     | 39.34    | 0.952    |
| VDN [42]                   | 39.26     | 0.955     | 39.38    | 0.952    |
| DANet [43]                 | 39.43     | 0.956     | 39.58    | 0.955    |
| **Unsupervised**           |           |           |          |          |
| GCBD [7]                   | -         | -         | 35.58    | 0.922    |
| C2N [19] + DIDN∗ [41]      | 35.35     | 0.937     | 37.28    | 0.924    |
| D-BSN [38] + MWCNN [28]    | -         | -         | 37.93    | 0.937    |
| **Self-supervised**        |           |           |          |          |
| Noise2Void [23]            | 27.68R    | 0.668R    | -        | -        |
| Noise2Self [3]             | 29.56R    | 0.808R    | -        | -        |
| NAC [40]                   | -         | -         | 36.20    | 0.925    |
| R2R [32]                   | 34.78     | 0.898     | -        | -        |
| **Proposed (AP-BSN)**      |           |           |          |          |
| AP-BSN                     | 34.90     | 0.900     | 37.46    | 0.924    |
| AP-BSN + R³                | 35.97     | 0.925     | 38.09    | 0.937    |
| AP-BSN† + R³               | 36.91     | 0.931     | -        | -        |

---

### **About the Model (AP-BSN)**
- **AP-BSN** is a **self-supervised denoising method** that uses only noisy images for training, making it highly practical for real-world scenarios where clean images are unavailable.
- It achieves competitive performance compared to supervised methods, especially when combined with refinements like **R³**.
- The method is trained in a **fully self-supervised fashion** on the SIDD benchmark, as indicated by the † symbol.

---
