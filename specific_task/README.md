# Specific Task: Heart Segmentation Model

(Project 1 – Coronary Artery Calcium Segmentation)

---

## Objective

The objective of this task is to develop an efficient deep learning model for volumetric heart segmentation from non-contrast CT scans. The goal is to approximate the segmentation quality of TotalSegmentator while achieving significantly faster inference.

---

## Dataset and Ground Truth

* Dataset: COCA (Cardiac CT dataset)
* Ground Truth: Generated using **TotalSegmentator**
* Number of Samples: **50 CT volumes**

This setup ensures reliable supervision while enabling efficient model training and evaluation.

---

## Methodology

### Model Architecture

A **3D U-Net architecture** was implemented for volumetric segmentation:

* Input: 3D CT volume (128 × 128 × 128)
* Output: Binary segmentation mask (heart region)

### Key Design Choices

* Volumetric processing captures **3D spatial context**
* Lightweight architecture ensures **fast inference**
* Suitable for medical segmentation with limited data

---

## Training Pipeline

### Preprocessing

* Resizing to fixed resolution (128³)
* **HU Windowing**: [-100, 400] → normalized to [0, 1]
* Intensity normalization

### Data Augmentation

* Random flips (all spatial axes)
* Random rotations (90°)

### Data Split

* Train: 80%
* Validation: 10%
* Test: 10%

---

## Loss Function

A hybrid loss was used:

[
\mathcal{L} = 0.7 \cdot \mathcal{L}*{Dice} + 0.3 \cdot \mathcal{L}*{BCE}
]

This balances:

* Overlap accuracy (Dice)
* Training stability (BCE)

---

## Results

* **Final Test Dice Score:** 0.9168
* **Average Inference Time per Volume:** 0.0796 seconds

The model significantly surpasses the required Dice threshold (>0.85) while maintaining fast inference.

Additionally, results remain consistent across runs after fixing random seed, indicating stable model performance.

---

## Qualitative Results

Representative predictions:

![Sample 1](results/images/sample1.png)
![Sample 2](results/images/sample2.png)

The model demonstrates strong localization and accurate segmentation of the heart region across different samples.

---

## Evaluation Summary

| Metric         | Value      |
| -------------- | ---------- |
| Dice Score     | 0.9168     |
| Inference Time | 0.0796 sec |
| Dataset Size   | 50 volumes |

---

## Model Weights

Model weights are available at:

```
specific_task/model/best_model.pth
```

---

## Key Observations

* Strong balance between **accuracy and efficiency**
* Post-processing (largest connected component) reduces noise
* Hybrid loss improves convergence and robustness

---

## Justification

A 3D U-Net was selected due to its effectiveness in capturing volumetric context while remaining computationally efficient. Compared to heavier segmentation models, it provides an optimal trade-off between segmentation accuracy and inference speed, making it suitable for real-world deployment scenarios.

---

## Conclusion

This task demonstrates the successful development of a fast, reliable, and high-performing 3D segmentation model capable of approximating TotalSegmentator outputs while being significantly more efficient.

