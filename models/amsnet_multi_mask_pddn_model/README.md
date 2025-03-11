# AMSNet Multi-Mask PDDN Model

This directory contains the implementation of the **AMSNet Multi-Mask PDDN Model**, a variant of the AMSNet framework designed for **self-supervised real image denoising**. The model leverages a **multi-mask scheme** to enhance denoising performance, particularly for real-world noisy images.


## Overview
The **AMSNet Multi-Mask PDDN Model** extends the original AMSNet framework by incorporating a **multi-mask scheme** to generate diverse training pairs from single noisy images. This approach improves the model's ability to generalize to real-world noise patterns, making it highly effective for practical denoising tasks.

---

## Model Architecture
The architecture of the AMSNet Multi-Mask PDDN Model consists of the following key components:
1. **Asymmetric Mask Generator**: Generates multiple masks to create diverse training pairs.
2. **Denoising Network**: A deep neural network trained to predict clean images from noisy inputs.
3. **Multi-Mask Fusion Module**: Combines outputs from multiple masks to produce the final denoised image.

For more details, refer to the [paper](#citation).

