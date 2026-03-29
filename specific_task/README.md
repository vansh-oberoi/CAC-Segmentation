# Specific Task: Heart Segmentation Model  
*(Project 1 – Coronary Artery Calcium Segmentation)*

---

## Objective

The objective of this task is to develop an efficient deep learning model for volumetric heart segmentation from non-contrast CT scans. The goal is to approximate the segmentation quality of TotalSegmentator while achieving significantly faster inference suitable for practical deployment.

---

## Dataset and Ground Truth

- **Dataset:** COCA (Cardiac CT dataset)  
- **Ground Truth:** Generated using **TotalSegmentator**  
- **Number of Samples:** 50 CT volumes  

This setup provides reliable supervision while allowing efficient experimentation on a moderate-scale dataset.

---

## Methodology

### Model Architecture

A **3D U-Net architecture** was implemented for volumetric segmentation:

- **Input:** 3D CT volume (128 × 128 × 128)  
- **Output:** Binary segmentation mask (heart region)  

### Key Design Choices

- Volumetric processing captures **3D spatial context**, essential for anatomical structures  
- Encoder–decoder structure enables **multi-scale feature learning**  
- Skip connections preserve **fine-grained boundary details**  
- Lightweight design ensures **fast inference without significant accuracy trade-off**

---

## Training Pipeline

### Preprocessing

- Resizing to fixed resolution (128³)  
- **HU Windowing:** [-100, 400] → normalized to [0, 1]  
- Intensity normalization for stable learning  

### Data Augmentation

- Random flips across spatial axes  
- Random 90° rotations  

These augmentations improve generalization while maintaining anatomical consistency.

---

## Data Split

- **Train:** 80%  
- **Validation:** 10%  
- **Test:** 10%  

---

## Loss Function

A hybrid loss formulation was used:

L = 0.7 * L_Dice + 0.3 * L_BCE

This balances:

- **Dice Loss:** Optimizes segmentation overlap  
- **Binary Cross-Entropy:** Improves training stability  

---

## Results

- **Final Test Dice Score:** **0.9168** *(primary evaluation on held-out test set)*  
- **Full Dataset Dice:** **0.9417** *(supplementary evaluation)*  
- **Average Inference Time per Volume:** **~0.08–0.09 seconds**  

The model significantly surpasses the required Dice threshold (>0.85) while maintaining efficient inference.

---

## Qualitative Results

Representative segmentation outputs:

![Sample 1](results/images/sample1.png)  
![Sample 2](results/images/sample2.png)

The model demonstrates strong localization and accurate segmentation across different samples, with minimal false positives.

---

## Evaluation Summary

| Metric                     | Value        |
|--------------------------|-------------|
| Dice Score (Test Set)    | 0.9168      |
| Dice Score (Full Eval)   | 0.9417      |
| Inference Time           | ~0.08–0.09 sec |
| Dataset Size             | 50 volumes  |

---

## Model Weights

The trained model is available at:# Specific Task: Heart Segmentation Model  
*(Project 1 – Coronary Artery Calcium Segmentation)*

---

## Objective

The objective of this task is to develop an efficient deep learning model for volumetric heart segmentation from non-contrast CT scans. The goal is to approximate the segmentation quality of TotalSegmentator while achieving significantly faster inference suitable for practical deployment.

---

## Dataset and Ground Truth

- **Dataset:** COCA (Cardiac CT dataset)  
- **Ground Truth:** Generated using **TotalSegmentator**  
- **Number of Samples:** 50 CT volumes  

This setup provides reliable supervision while allowing efficient experimentation on a moderate-scale dataset.

---

## Methodology

### Model Architecture

A **3D U-Net architecture** was implemented for volumetric segmentation:

- **Input:** 3D CT volume (128 × 128 × 128)  
- **Output:** Binary segmentation mask (heart region)  

### Key Design Choices

- Volumetric processing captures **3D spatial context**, essential for anatomical structures  
- Encoder–decoder structure enables **multi-scale feature learning**  
- Skip connections preserve **fine-grained boundary details**  
- Lightweight design ensures **fast inference without significant accuracy trade-off**

---

## Training Pipeline

### Preprocessing

- Resizing to fixed resolution (128³)  
- **HU Windowing:** [-100, 400] → normalized to [0, 1]  
- Intensity normalization for stable learning  

### Data Augmentation

- Random flips across spatial axes  
- Random 90° rotations  

These augmentations improve generalization while maintaining anatomical consistency.

---

## Data Split

- **Train:** 80%  
- **Validation:** 10%  
- **Test:** 10%  

---

## Loss Function

A hybrid loss formulation was used:

\[
\mathcal{L} = 0.7 \cdot \mathcal{L}_{Dice} + 0.3 \cdot \mathcal{L}_{BCE}
\]

This balances:

- **Dice Loss:** Optimizes segmentation overlap  
- **Binary Cross-Entropy:** Improves training stability  

---

## Results

- **Final Test Dice Score:** **0.9168** *(primary evaluation on held-out test set)*  
- **Full Dataset Dice:** **0.9417** *(supplementary evaluation)*  
- **Average Inference Time per Volume:** **~0.08–0.09 seconds**  

The model significantly surpasses the required Dice threshold (>0.85) while maintaining efficient inference.

---

## Qualitative Results

Representative segmentation outputs:

![Sample 1](results/images/sample1.png)  
![Sample 2](results/images/sample2.png)

The model demonstrates strong localization and accurate segmentation across different samples, with minimal false positives.

---

## Evaluation Summary

| Metric                     | Value        |
|--------------------------|-------------|
| Dice Score (Test Set)    | 0.9168      |
| Dice Score (Full Eval)   | 0.9417      |
| Inference Time           | ~0.08–0.09 sec |
| Dataset Size             | 50 volumes  |

---

## Model Weights

The trained model is available at:`specific_task/model.pth`

or download directly:
https://github.com/vansh-oberoi/CAC-Segmentation/blob/main/specific_task/model.pth

---

## Key Observations

- Strong balance between **accuracy and computational efficiency**  
- **HU windowing** ensures consistent intensity representation  
- **Largest connected component filtering** reduces false positives  
- Hybrid loss improves convergence and robustness under class imbalance  

---

## Model Choice Justification

A 3D U-Net was selected due to its strong capability in modeling volumetric spatial dependencies inherent in medical imaging data. Unlike 2D approaches, it effectively captures inter-slice continuity, which is crucial for accurate anatomical segmentation. The encoder–decoder design enables hierarchical feature extraction, while skip connections preserve spatial resolution for precise boundary delineation. Additionally, the architecture remains computationally efficient, making it suitable for moderate-sized datasets and real-time inference constraints. The hybrid Dice and Binary Cross-Entropy loss further enhances performance by balancing overlap accuracy with training stability.

---

## Conclusion

This work demonstrates the development of a fast, reliable, and high-performing 3D segmentation model. The proposed approach achieves strong agreement with TotalSegmentator outputs while significantly reducing inference time, making it well-suited for scalable and real-world medical imaging applications.
