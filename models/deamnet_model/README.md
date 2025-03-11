

# **Denoising Project**

This repository focuses on image denoising, specifically evaluating methods for Gaussian noise removal. The results are benchmarked on datasets like **Set12**, **BSD68**, and **Urban100**, with noise levels of **15**, **25**, and **50**.

---

## **Results**

### **Table 4: Quantitative Comparison Results**
The table below shows the **PSNR (Peak Signal-to-Noise Ratio)** and **SSIM (Structural Similarity Index Measure)** results for various denoising methods across different noise levels.

| Method          | Noise Level 15                     | Noise Level 25                     | Noise Level 50                     |
|-----------------|------------------------------------|------------------------------------|------------------------------------|
|                 | Set12   | BSD68  | Urban100 | Set12   | BSD68  | Urban100 | Set12   | BSD68  | Urban100 |
| **BM3D [11]**   | 32.37   | 31.07  | 32.35    | 29.97   | 28.57  | 29.70    | 26.72   | 25.62  | 25.95    |
|                 | 0.8952  | 0.8717 | 0.9220   | 0.8504  | 0.8013 | 0.8777   | 0.7676  | 0.6864 | 0.7791   |
| **WNNM [19]**   | 32.70   | 31.37  | 32.97    | 30.28   | 28.83  | 30.39    | 27.05   | 25.87  | 26.83    |
|                 | 0.8982  | 0.8766 | 0.9271   | 0.8577  | 0.8087 | 0.8885   | 0.7775  | 0.6982 | 0.8047   |
| **TNRD [9]**    | 32.50   | 31.42  | 31.86    | 30.06   | 28.92  | 29.25    | 26.82   | 25.97  | 25.88    |
|                 | 0.8958  | 0.8769 | 0.9031   | 0.8512  | 0.8093 | 0.8473   | 0.768   | 0.6994 | 0.7563   |
| **DnCNN [61]**  | 32.86   | 31.73  | 32.68    | 30.44   | 29.23  | 29.97    | 27.18   | 26.23  | 26.28    |
|                 | 0.9031  | 0.8907 | 0.9255   | 0.8622  | 0.8278 | 0.8797   | 0.7829  | 0.7189 | 0.7874   |
| **FFDNet [62]** | 32.75   | 31.63  | 32.43    | 30.43   | 29.19  | 29.92    | 27.32   | 26.29  | 26.52    |
|                 | 0.9027  | 0.8902 | 0.9273   | 0.8634  | 0.8289 | 0.8886   | 0.7903  | 0.7245 | 0.8057   |
| **RED [34]**    | -       | -      | -        | -       | -      | -        | 27.34   | 26.35  | 26.48    |
|                 | -       | -      | -        | -       | -      | -        | 0.7897  | 0.7245 | 0.7991   |
| **MemNet [47]** | -       | -      | -        | -       | -      | -        | 27.38   | 26.35  | 26.64    |
|                 | -       | -      | -        | -       | -      | -        | 0.7933  | 0.7297 | 0.8029   |
| **UNLNet [28]** | 32.69   | 31.47  | 32.47    | 30.27   | 28.96  | 29.80    | 27.07   | 26.04  | 26.14    |
|                 | 0.9001  | 0.8858 | 0.9252   | 0.8576  | 0.8197 | 0.8831   | 0.7793  | 0.7129 | 0.7911   |
| **CFSNet [53]** | 32.48   | 31.29  | 32.12    | 30.44   | 29.24  | 29.91    | 27.22   | 26.28  | 26.36    |
|                 | 0.8905  | 0.8694 | 0.9138   | 0.8623  | 0.8290 | 0.8848   | 0.7855  | 0.7206 | 0.7934   |
| **N3Net [41]**  | -       | -      | -        | 30.50   | 29.30  | 30.19    | 27.43   | 26.39  | 26.82    |
|                 | -       | -      | -        | 0.8651  | 0.8329 | 0.8910   | 0.7950  | 0.7302 | 0.8141   |
| **ADNet [49]**  | 32.98   | 31.74  | 32.87    | 30.58   | 29.25  | 30.24    | 27.37   | 26.29  | 26.64    |
|                 | 0.9050  | 0.8916 | 0.9308   | 0.8654  | 0.8294 | 0.8923   | 0.7908  | 0.7216 | 0.8073   |
| **BRDNet [50]** | 33.03   | 31.79  | 33.02    | 30.61   | 29.29  | 30.37    | 27.45   | 26.36  | 26.82    |
|                 | 0.9055  | 0.8926 | 0.9322   | 0.8657  | 0.8309 | 0.8934   | 0.7935  | 0.7265 | 0.8131   |
| **RIDNet [3]**  | 32.91   | 31.81  | 33.11    | 30.60   | 29.34  | 30.49    | 27.43   | 26.40  | 26.73    |
|                 | 0.9059  | 0.8934 | 0.9339   | 0.8672  | 0.8331 | 0.8975   | 0.7932  | 0.7267 | 0.8132   |
| **DeamNet**     | 33.19   | 31.91  | 33.37    | 30.81   | 29.44  | 30.85    | 27.74   | 26.54  | 27.53    |
|                 | 0.9097  | 0.8957 | 0.9372   | 0.8717  | 0.8373 | 0.9048   | 0.8057  | 0.7368 | 0.8373   |
| **DeamNet***    | 33.21   | 31.93  | 33.45    | 30.86   | 29.46  | 30.95    | 27.81   | 26.57  | 27.66    |
|                 | 0.9098  | 0.8959 | 0.9375   | 0.8720  | 0.8374 | 0.9056   | 0.8067  | 0.7370 | 0.8400   |

---

### **Key Observations**
1. **Traditional Methods (BM3D, WNNM)**:
   - Perform well but are generally outperformed by deep learning-based methods.

2. **Deep Learning Methods (DnCNN, FFDNet, ADNet, etc.)**:
   - Consistently achieve higher PSNR and SSIM values across all noise levels.
   - **DeamNet** and **DeamNet*** (with enhancements) achieve the best results, especially at higher noise levels (σ = 50).

3. **DeamNet**:
   - Outperforms all other methods, demonstrating the effectiveness of its adaptive consistency prior.

---

## **Paper Link**
The paper associated with this work can be accessed here:  
[Adaptive Consistency Prior Based Deep Network for Image Denoising (CVPR 2021)](https://openaccess.thecvf.com/content/CVPR2021/papers/Ren_Adaptive_Consistency_Prior_Based_Deep_Network_for_Image_Denoising_CVPR_2021_paper.pdf)

---

Let me know if you need further adjustments!Here’s the updated **GitHub README** based on the new table and paper link. This version excludes the **Usage** and **Citation** sections, as requested, and includes the **paper link**:

---

# **Denoising Project**

This repository focuses on image denoising, specifically evaluating methods for Gaussian noise removal. The results are benchmarked on datasets like **Set12**, **BSD68**, and **Urban100**, with noise levels of **15**, **25**, and **50**.

---

## **Results**

### **Table 4: Quantitative Comparison Results**
The table below shows the **PSNR (Peak Signal-to-Noise Ratio)** and **SSIM (Structural Similarity Index Measure)** results for various denoising methods across different noise levels.

| Method          | Noise Level 15                     | Noise Level 25                     | Noise Level 50                     |
|-----------------|------------------------------------|------------------------------------|------------------------------------|
|                 | Set12   | BSD68  | Urban100 | Set12   | BSD68  | Urban100 | Set12   | BSD68  | Urban100 |
| **BM3D [11]**   | 32.37   | 31.07  | 32.35    | 29.97   | 28.57  | 29.70    | 26.72   | 25.62  | 25.95    |
|                 | 0.8952  | 0.8717 | 0.9220   | 0.8504  | 0.8013 | 0.8777   | 0.7676  | 0.6864 | 0.7791   |
| **WNNM [19]**   | 32.70   | 31.37  | 32.97    | 30.28   | 28.83  | 30.39    | 27.05   | 25.87  | 26.83    |
|                 | 0.8982  | 0.8766 | 0.9271   | 0.8577  | 0.8087 | 0.8885   | 0.7775  | 0.6982 | 0.8047   |
| **TNRD [9]**    | 32.50   | 31.42  | 31.86    | 30.06   | 28.92  | 29.25    | 26.82   | 25.97  | 25.88    |
|                 | 0.8958  | 0.8769 | 0.9031   | 0.8512  | 0.8093 | 0.8473   | 0.768   | 0.6994 | 0.7563   |
| **DnCNN [61]**  | 32.86   | 31.73  | 32.68    | 30.44   | 29.23  | 29.97    | 27.18   | 26.23  | 26.28    |
|                 | 0.9031  | 0.8907 | 0.9255   | 0.8622  | 0.8278 | 0.8797   | 0.7829  | 0.7189 | 0.7874   |
| **FFDNet [62]** | 32.75   | 31.63  | 32.43    | 30.43   | 29.19  | 29.92    | 27.32   | 26.29  | 26.52    |
|                 | 0.9027  | 0.8902 | 0.9273   | 0.8634  | 0.8289 | 0.8886   | 0.7903  | 0.7245 | 0.8057   |
| **RED [34]**    | -       | -      | -        | -       | -      | -        | 27.34   | 26.35  | 26.48    |
|                 | -       | -      | -        | -       | -      | -        | 0.7897  | 0.7245 | 0.7991   |
| **MemNet [47]** | -       | -      | -        | -       | -      | -        | 27.38   | 26.35  | 26.64    |
|                 | -       | -      | -        | -       | -      | -        | 0.7933  | 0.7297 | 0.8029   |
| **UNLNet [28]** | 32.69   | 31.47  | 32.47    | 30.27   | 28.96  | 29.80    | 27.07   | 26.04  | 26.14    |
|                 | 0.9001  | 0.8858 | 0.9252   | 0.8576  | 0.8197 | 0.8831   | 0.7793  | 0.7129 | 0.7911   |
| **CFSNet [53]** | 32.48   | 31.29  | 32.12    | 30.44   | 29.24  | 29.91    | 27.22   | 26.28  | 26.36    |
|                 | 0.8905  | 0.8694 | 0.9138   | 0.8623  | 0.8290 | 0.8848   | 0.7855  | 0.7206 | 0.7934   |
| **N3Net [41]**  | -       | -      | -        | 30.50   | 29.30  | 30.19    | 27.43   | 26.39  | 26.82    |
|                 | -       | -      | -        | 0.8651  | 0.8329 | 0.8910   | 0.7950  | 0.7302 | 0.8141   |
| **ADNet [49]**  | 32.98   | 31.74  | 32.87    | 30.58   | 29.25  | 30.24    | 27.37   | 26.29  | 26.64    |
|                 | 0.9050  | 0.8916 | 0.9308   | 0.8654  | 0.8294 | 0.8923   | 0.7908  | 0.7216 | 0.8073   |
| **BRDNet [50]** | 33.03   | 31.79  | 33.02    | 30.61   | 29.29  | 30.37    | 27.45   | 26.36  | 26.82    |
|                 | 0.9055  | 0.8926 | 0.9322   | 0.8657  | 0.8309 | 0.8934   | 0.7935  | 0.7265 | 0.8131   |
| **RIDNet [3]**  | 32.91   | 31.81  | 33.11    | 30.60   | 29.34  | 30.49    | 27.43   | 26.40  | 26.73    |
|                 | 0.9059  | 0.8934 | 0.9339   | 0.8672  | 0.8331 | 0.8975   | 0.7932  | 0.7267 | 0.8132   |
| **DeamNet**     | 33.19   | 31.91  | 33.37    | 30.81   | 29.44  | 30.85    | 27.74   | 26.54  | 27.53    |
|                 | 0.9097  | 0.8957 | 0.9372   | 0.8717  | 0.8373 | 0.9048   | 0.8057  | 0.7368 | 0.8373   |
| **DeamNet***    | 33.21   | 31.93  | 33.45    | 30.86   | 29.46  | 30.95    | 27.81   | 26.57  | 27.66    |
|                 | 0.9098  | 0.8959 | 0.9375   | 0.8720  | 0.8374 | 0.9056   | 0.8067  | 0.7370 | 0.8400   |

---

### **Key Observations**
1. **Traditional Methods (BM3D, WNNM)**:
   - Perform well but are generally outperformed by deep learning-based methods.

2. **Deep Learning Methods (DnCNN, FFDNet, ADNet, etc.)**:
   - Consistently achieve higher PSNR and SSIM values across all noise levels.
   - **DeamNet** and **DeamNet*** (with enhancements) achieve the best results, especially at higher noise levels (σ = 50).

3. **DeamNet**:
   - Outperforms all other methods, demonstrating the effectiveness of its adaptive consistency prior.

---

## **Paper Link**
The paper associated with this work can be accessed here:  
[Adaptive Consistency Prior Based Deep Network for Image Denoising (CVPR 2021)](https://openaccess.thecvf.com/content/CVPR2021/papers/Ren_Adaptive_Consistency_Prior_Based_Deep_Network_for_Image_Denoising_CVPR_2021_paper.pdf)

---
