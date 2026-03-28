from monai.transforms import *

# ---------------------------------------------------------
# Preprocessing pipeline for 3D CT volumes
# ---------------------------------------------------------
# Designed specifically for CAC segmentation
# Includes spatial standardization, HU-based intensity scaling,
# and data augmentation for robust learning
# ---------------------------------------------------------

def get_train_transforms():
    return Compose([
        LoadImaged(keys=["image", "label"]),
        EnsureChannelFirstd(keys=["image", "label"]),

        ResizeD(keys=["image", "label"], spatial_size=(128,128,128)),

        # HU windowing + normalization
        ScaleIntensityRanged(
            keys=["image"],
            a_min=-100,
            a_max=400,
            b_min=0.0,
            b_max=1.0,
            clip=True
        ),

        # Data augmentation
        RandFlipd(keys=["image", "label"], prob=0.5, spatial_axis=0),
        RandFlipd(keys=["image", "label"], prob=0.5, spatial_axis=1),
        RandFlipd(keys=["image", "label"], prob=0.5, spatial_axis=2),

        RandRotate90d(keys=["image", "label"], prob=0.5, max_k=3),
    ])


def get_val_transforms():
    return Compose([
        LoadImaged(keys=["image", "label"]),
        EnsureChannelFirstd(keys=["image", "label"]),
        ResizeD(keys=["image", "label"], spatial_size=(128,128,128)),

        ScaleIntensityRanged(
            keys=["image"],
            a_min=-100,
            a_max=400,
            b_min=0.0,
            b_max=1.0,
            clip=True
        ),
    ])
