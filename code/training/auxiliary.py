import os
import shutil
import random
import torchvision
import torch
from torch.utils import data


def create_sets(original_folder_path):
    training_folder_path = "sets/training"
    validation_folder_path = "sets/validation"
    test_folder_path = "sets/test"

    os.makedirs(training_folder_path, exist_ok=True)
    os.makedirs(validation_folder_path, exist_ok=True)
    os.makedirs(test_folder_path, exist_ok=True)

    # List all directories in the original folder
    directories = os.listdir(original_folder_path)

    # Move directories to the new folders
    for i, directory in enumerate(directories):
        images = os.listdir(os.path.join(original_folder_path, directory))
        total_images = len(images)
        training_count = int(total_images * 0.7)
        validation_count = int(total_images * 0.2)

        for j in range(int(total_images)):
            if j < training_count:
                destination_path = os.path.join(training_folder_path, directory)
            elif j < training_count + validation_count:
                destination_path = os.path.join(validation_folder_path, directory)
            else:
                destination_path = os.path.join(test_folder_path, directory)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            shutil.copy(os.path.join(original_folder_path, directory, images[j]), destination_path)


def create_dataloader(set_path, transform, batch_size=1024):
    set_data = torchvision.datasets.ImageFolder(root=set_path, transform=transform)
    set_loader = data.DataLoader(set_data, batch_size=batch_size, shuffle=True, num_workers=2, prefetch_factor=4,
                                 pin_memory=True, persistent_workers=True)
    return set_loader


def get_device(seed):
    if torch.cuda.is_available():
        device = torch.device('cuda')
        torch.cuda.manual_seed(seed)
    else:
        device = torch.device('cpu')
    return device
