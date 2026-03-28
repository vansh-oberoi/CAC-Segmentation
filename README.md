# Heart Segmentation using 3D U-Net (ML4SCI Evaluation Task)

This repository presents an end-to-end 3D medical image segmentation pipeline developed as part of the ML4SCI (PrediCT) evaluation tasks. The work focuses on preprocessing CT volumes and training a model for accurate and efficient heart segmentation.

---

## Task Breakdown

The evaluation consists of two components:

- **Common Task:** COCA Dataset Preprocessing  
- **Specific Task:** Heart Segmentation Model  

---

# Common Task: COCA Dataset Preprocessing

## Objective
Build a preprocessing and data loading pipeline tailored for 3D medical imaging tasks.

## Implementation

The following pipeline was developed:

- Processed **COCA dataset** CT volumes  
- Applied **HU windowing** for cardiac CT  
- Performed **normalization and resizing**  
- Created **train / validation / test split**  
- Implemented efficient **3D data loader**  
- Generated **ground truth masks using TotalSegmentator**  

## Outcome

A complete preprocessing pipeline enabling efficient and reproducible training on volumetric CT data.

---

# Specific Task: Heart Segmentation Model

## Objective

- Train a segmentation model  
- Achieve Dice score > 0.85  
- Ensure faster inference than TotalSegmentator  

---

## Model

A **3D U-Net architecture** was implemented to capture spatial context in volumetric data.

---

## Training Details

- Dataset: **50 CT volumes with corresponding masks**  
- Loss Function:
  - Dice Loss  
  - Binary Cross-Entropy (BCE)  
- Data augmentation:
  - Flips  
  - Rotations  

---

## Post-processing

- Connected component filtering  
- Threshold optimization  

These steps helped reduce noise and improve segmentation quality.

---

# Results

| Metric | Value |
|--------|------|
| Dice Score | **0.8875** |
| Inference Time | **0.083 sec per volume** |

---

## Observations

- Achieved Dice score **above required threshold (>0.85)**  
- Fast inference compared to heavy segmentation models  
- Stable performance despite class imbalance  

---

# Qualitative Results

Representative outputs include:

- Input CT slices  
- Ground truth masks  
- Predicted segmentation  

(Add images in `results/images/`)

---

# Repository Structure

---

# Reproducibility

The pipeline is modular and reproducible:

- Structured preprocessing pipeline  
- Consistent training setup  
- Clear evaluation metrics  

---

# Proposed GSoC Extension

A key limitation of standard segmentation models is **false positives in anatomically irrelevant regions**.

To address this, the proposed extension introduces a:

## Context-Constrained Segmentation Framework

### Key Idea

- Learn **what to segment** (target region)  
- Learn **where it is valid** (anatomical context)  

### Approach

- Dual-branch architecture:
  - Segmentation branch (local features)  
  - Context branch (global prior)  

- Consistency constraint:

L = L_seg + λ || P_seg · (1 − P_context) ||

This enforces anatomically consistent predictions and reduces false positives.

---

# Future Work

- Integrate anatomical constraints into training  
- Reduce false positives using context modeling  
- Extend toward clinical metrics (e.g., CAC scoring)  
- Scale to larger datasets  

---

# Tech Stack

- Python  
- PyTorch  
- NumPy  
- Medical Imaging (NIfTI)  

---

# Author

**Vansh Oberoi**
