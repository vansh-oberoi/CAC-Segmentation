from monai.data import Dataset, DataLoader

# ---------------------------------------------------------
# DataLoader for efficient 3D medical image training
# ---------------------------------------------------------
# Separates data handling from training logic
# Ensures reproducibility and modular pipeline design
# ---------------------------------------------------------

def get_dataloaders(train_files, val_files, test_files, train_transforms, val_transforms):

    train_ds = Dataset(train_files, transform=train_transforms)
    val_ds   = Dataset(val_files, transform=val_transforms)
    test_ds  = Dataset(test_files, transform=val_transforms)

    # Batch size = 1 due to memory constraints of 3D volumes
    train_loader = DataLoader(train_ds, batch_size=1, shuffle=True)
    val_loader   = DataLoader(val_ds, batch_size=1, shuffle=False)
    test_loader  = DataLoader(test_ds, batch_size=1, shuffle=False)

    return train_loader, val_loader, test_loader
