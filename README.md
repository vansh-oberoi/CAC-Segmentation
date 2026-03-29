# Heart Segmentation using 3D U-Net (ML4SCI Evaluation Task)

> Achieved **Dice score of 0.9168 on held-out test set** and **0.9417 on full evaluation**, surpassing baseline requirements (>0.85) while maintaining fast inference.

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
- Applied **HU windowing** for cardiac CT ([-100, 400])  
- Normalized intensities to **[0, 1]**  
- Resized volumes to **128 × 128 × 128**  
- Created **train / validation / test split (80/10/10)**  
- Implemented efficient **3D data loaders (MONAI + PyTorch)**  
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
  - Random flips  
  - Random rotations  

---

## Post-processing

- Largest connected component filtering  
- Threshold optimization  

These steps reduce noise and improve segmentation quality.

---

# Results

| Metric | Value |
|--------|------|
| **Dice Score (Test Set)** | **0.9168** |
| **Dice Score (Full Evaluation)** | **0.9417** |
| **Inference Time** | **~0.08–0.09 sec per volume** |

✔ Surpasses required Dice (>0.85)  
✔ Maintains fast and efficient inference  

---

## Why the Approach Works

- **3D U-Net captures volumetric spatial context effectively**  
- **HU windowing enhances cardiac region visibility**  
- **Hybrid loss (Dice + BCE)** balances accuracy and stability  
- **Post-processing reduces false positives**  

This ensures both **high accuracy and robustness**.

---

## Qualitative Results

Each visualization shows:
- Left: Input CT slice  
- Middle: Ground truth mask  
- Right: Model prediction overlay  

### Sample 1
![Sample 1](../results/images/Sample1.png)

### Sample 2
![Sample 2](../results/images/Sample2.png)

### Sample 3
![Sample 3](../results/images/Sample3.png)

---

## Repository Structure

CAC-Segmentation/
|
|-- common_task/ # Preprocessing and data loading
|-- specific_task/ # Model, training, evaluation
|-- results/images/# Output visualizations and Plots
|-- README.md -- requirements.txt


---

## Reproducibility

The pipeline is modular and reproducible:

- Structured preprocessing pipeline  
- Consistent training configuration  
- Clear evaluation setup  

---

# Proposed GSoC Extension

A key limitation of standard segmentation models is **false positives in anatomically irrelevant regions**.

## Context-Constrained Segmentation Framework

### Key Idea

- Learn **what to segment** (target region)  
- Learn **where it is valid** (anatomical context)  

### Approach

- Dual-branch architecture:
  - Segmentation branch (local features)  
  - Context branch (global anatomical prior)  

- Consistency constraint:

 L = L_seg + λ || P_seg · (1 − P_context) ||

 
This enforces **anatomical consistency** and reduces false positives.

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
- MONAI  
- 3D Slicer
- Pydicom
- NIfTI Medical Imaging  

---

# Note

This repository demonstrates not only model performance but also a clear understanding of medical imaging pipelines, optimization strategies, and real-world constraints such as inference efficiency and data imbalance.

---

# Author

**Vansh Oberoi**
