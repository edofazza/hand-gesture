import os
import shutil
import random
import torchvision
from torch.utils import data


def create_sets(original_folder_path):
    training_folder_path = "./training"
    validation_folder_path = "./validation"
    test_folder_path = "./test"

    os.makedirs(training_folder_path, exist_ok=True)
    os.makedirs(validation_folder_path, exist_ok=True)
    os.makedirs(test_folder_path, exist_ok=True)

    # List all directories in the original folder
    directories = os.listdir(original_folder_path)

    # Randomly shuffle the directories
    random.shuffle(directories)

    # Calculate the number of directories for each new directory
    total_directories = len(directories)
    training_count = int(total_directories * 0.7)
    validation_count = int(total_directories * 0.2)
    test_count = total_directories - training_count - validation_count

    # Move directories to the new folders
    for i, directory in enumerate(directories):
        source_path = os.path.join(original_folder_path, directory)

        if i < training_count:
            destination_path = os.path.join(training_folder_path, directory)
        elif i < training_count + validation_count:
            destination_path = os.path.join(validation_folder_path, directory)
        else:
            destination_path = os.path.join(test_folder_path, directory)

        # Move the directory
        shutil.move(source_path, destination_path)


def create_dataloaders(train_path, val_path, test_path, transform, batch_size=1024):
    train_data = torchvision.datasets.ImageFolder(root=train_path, transform=transform)
    val_data = torchvision.datasets.ImageFolder(root=val_path, transform=transform)
    test_data = torchvision.datasets.ImageFolder(root=test_path, transform=transform)
    train_loader = data.Dataloader(train_data, batch_size=batch_size, shuffle=True)
    val_loader = data.Dataloader(val_data, batch_size=batch_size, shuffle=True)
    test_loader = data.Dataloader(test_data, batch_size=batch_size, shuffle=True)
    return train_loader, val_loader, test_loader


