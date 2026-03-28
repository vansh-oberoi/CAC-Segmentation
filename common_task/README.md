# Common Task: Preprocessing and Data Pipeline

## Overview

This section implements the required preprocessing and data loading pipeline for 3D medical image segmentation using volumetric CT data. The pipeline is specifically tailored for Coronary Artery Calcium (CAC) segmentation.

---

## Preprocessing Pipeline

The preprocessing pipeline is implemented using MONAI and includes:

- Spatial standardization of all volumes to a fixed size (128 × 128 × 128)
- HU-based intensity scaling (windowing + normalization)
- Data augmentation:
  - Random flips across all spatial axes
  - Random 90° rotations

These steps ensure consistent input representation and improve model generalization.

---

## Data Loading

Efficient data loading is implemented using MONAI’s Dataset and PyTorch DataLoader.

- Batch size: 1 (due to memory constraints of 3D volumes)
- Shuffling applied during training
- Separate loaders for train, validation, and test sets

---

## Dataset Split

The dataset is divided as follows:

- Training set: 80%
- Validation set: 10%
- Test set: 10%

This ensures unbiased model evaluation.

---

## Dataset Statistics

- Total volumes: 50
- Training set: 40 volumes
- Validation set: 5 volumes
- Test set: 5 volumes
- Data format: NIfTI (.nii)
- Modality: Non-contrast CT
- Task: Binary segmentation

---

## Justification

A complete preprocessing and data loading pipeline was developed for 3D medical image segmentation using volumetric CT data. The pipeline is tailored for CAC segmentation, where both spatial consistency and intensity normalization are critical.

HU-based intensity windowing was applied to enhance contrast between calcified regions and surrounding tissues. This improves model sensitivity to small and sparse CAC regions. Additionally, augmentation techniques such as flips and rotations were incorporated to improve robustness across spatial variations.

The pipeline is implemented using MONAI to ensure efficiency and reproducibility. Class imbalance is handled through loss design (Dice + BCE) and exposure to diverse samples during training. Overall, the pipeline balances computational efficiency with strong segmentation performance.
