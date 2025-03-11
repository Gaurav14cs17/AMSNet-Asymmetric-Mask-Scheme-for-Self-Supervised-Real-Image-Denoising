# **Denoising Project**

This repository contains the implementation of a denoising method for Gaussian noise removal. The method is evaluated on standard datasets (KODAK, BSD300, SET14) and compared against baselines like **N2C (Noise2Clean)**, **N2N (Noise2Noise)**, and **CBM3D**.

---

## **Results**

### **Table 1: Image Quality Results for Gaussian Noise**
The table below shows the **PSNR (Peak Signal-to-Noise Ratio)** results for Gaussian noise removal. Values of σ (noise level) are shown in 8-bit units.

| Noise Type | Method               | σ Known? | KODAK  | BSD300 | SET14  | Average |
|------------|----------------------|----------|--------|--------|--------|---------|
| **Gaussian σ = 25** |                      |          |        |        |        |         |
|            | Baseline, N2C        | no       | 32.46  | 31.08  | 31.26  | 31.60   |
|            | Baseline, N2N        | no       | 32.45  | 31.07  | 31.23  | 31.58   |
|            | Our                  | yes      | 32.45  | 31.03  | 31.25  | 31.57   |
|            | Our                  | no       | 32.44  | 31.02  | 31.22  | 31.56   |
|            | Our ablated, diag. Σ | yes      | 31.60  | 29.91  | 30.58  | 30.70   |
|            | Our ablated, diag. Σ | no       | 31.55  | 29.87  | 30.53  | 30.65   |
|            | Our ablated, µ only  | no       | 30.64  | 28.65  | 29.57  | 29.62   |
|            | CBM3D                | yes      | 31.82  | 30.40  | 30.68  | 30.96   |
|            | CBM3D                | no       | 31.81  | 30.40  | 30.66  | 30.96   |
| **Gaussian σ ∈ [5, 50]** |                      |          |        |        |        |         |
|            | Baseline, N2C        | no       | 32.57  | 31.29  | 31.27  | 31.71   |
|            | Baseline, N2N        | no       | 32.57  | 31.29  | 31.26  | 31.70   |
|            | Our                  | yes      | 32.47  | 31.19  | 31.21  | 31.62   |
|            | Our                  | no       | 32.46  | 31.18  | 31.13  | 31.59   |
|            | Our ablated, diag. Σ | yes      | 31.59  | 30.06  | 30.54  | 30.73   |
|            | Our ablated, diag. Σ | no       | 31.58  | 30.05  | 30.45  | 30.69   |
|            | Our ablated, µ only  | no       | 30.54  | 28.56  | 29.41  | 29.50   |
|            | CBM3D                | yes      | 31.99  | 30.67  | 30.78  | 31.15   |
|            | CBM3D                | no       | 31.99  | 30.67  | 30.72  | 31.13   |

---

### **Key Observations**
1. **Baselines (N2C and N2N)**:
   - Perform consistently well across all datasets.
   - Slightly outperform the proposed method in some cases.

2. **Proposed Method**:
   - Achieves competitive results, especially when the noise level (σ) is known.
   - Performs slightly worse than baselines when σ is unknown.

3. **Ablated Versions**:
   - **Diagonal Σ ablation**: Shows a significant drop in performance, indicating the importance of the full covariance matrix.
   - **µ-only ablation**: Performs the worst, highlighting the critical role of the mean estimation.

4. **CBM3D**:
   - A strong traditional method that performs well, especially when σ is known.

---

## **Datasets**
The model is evaluated on the following datasets:
- **KODAK**
- **BSD300**
- **SET14**


### **Paper Link**
The paper can be accessed here: [https://arxiv.org/pdf/1901.10277](https://arxiv.org/pdf/1901.10277).

---
