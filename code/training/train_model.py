import os
import torch
import torchvision.datasets
from torch.utils import data
from torchvision import transforms
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch import nn
from sklearn.metrics import f1_score, confusion_matrix, precision_score, recall_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
from decimal import Decimal
import shutil

from code.training.models import get_model
from code.training.auxiliary import create_sets, create_dataloader, get_device
from code.utils.performance import folder_to_zip

def train(train_loader, model, optimizer, criterion, device):
    model.train()
    train_loss = 0.0
    true_labels = []
    predicted_labels = []
    total = 0

    for images, labels in train_loader:
        optimizer.zero_grad()
        images, labels = images.to(device), labels.to(device)

        outputs = model(images)
        loss = criterion(outputs, labels)

        loss.backward()
        optimizer.step()

        train_loss += loss.item() * images.size(0)
        _, preds = torch.max(outputs.data, 1)
        true_labels.extend(labels.cpu().numpy())
        predicted_labels.extend(preds.cpu().numpy())
        total += labels.size(0)

    train_loss /= len(train_loader.dataset)
    train_acc = sum([1 for i, j in zip(true_labels, predicted_labels) if i == j]) / total
    train_f1 = f1_score(true_labels, predicted_labels, average='macro')

    print('Train loss: {:.3f}, Train accuracy: {:.3f}, Train Macro F1-score: {:.3f}'.format(train_loss, train_acc, train_f1))

    return train_loss, train_acc, train_f1


def test(test_loader, model, criterion, device):
    model.eval()
    test_loss = 0.0
    true_labels = []
    predicted_labels = []
    total = 0

    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            test_loss += loss.item() * images.size(0)
            _, preds = torch.max(outputs.data, 1)
            true_labels.extend(labels.cpu().numpy())
            predicted_labels.extend(preds.cpu().numpy())
            total += labels.size(0)

    test_loss /= len(test_loader.dataset)
    test_acc = sum([1 for i, j in zip(true_labels, predicted_labels) if i == j]) / total
    test_f1 = f1_score(true_labels, predicted_labels, average='macro')
    conf_matrix = confusion_matrix(true_labels, predicted_labels)

    print('Test loss: {:.3f}, Test accuracy: {:.3f}, Test Macro F1-score: {:.3f}'.format(test_loss, test_acc, test_f1))

    return test_loss, test_acc, test_f1, conf_matrix


def train_on_cifar(model_name, model, shape, device):
    transform_train = transforms.Compose([
        transforms.Resize(shape),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    transform_test = transforms.Compose([
        transforms.Resize(shape),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    train_dataset = torchvision.datasets.CIFAR10(root='.', train=True, transform=transform_train, download=True)
    test_dataset = torchvision.datasets.CIFAR10(root='.', train=False, transform=transform_test, download=True)

    train_loader = data.DataLoader(train_dataset, batch_size=64, shuffle=True, num_workers=4, prefetch_factor=8,
                                 pin_memory=True, persistent_workers=True)
    test_loader = data.DataLoader(test_dataset, batch_size=64, shuffle=False, num_workers=4, prefetch_factor=8,
                                 pin_memory=True, persistent_workers=True)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    best_loss = 999999
    convergence = 0

    for epoch in range(0, 500):
        print(f'Epoch: {epoch}')
        _ = train(
            train_loader,
            model,
            optimizer,
            criterion,
            device
        )
        test_loss, _, _, _ = test(test_loader, model, criterion, device)

        if test_loss <= best_loss:
            best_loss = test_loss
            print('Saving model')
            torch.save(model.state_dict(), os.path.join('models', model_name, f'{model_name}.pkl'))
            convergence = 0
        else:
            convergence += 1

        if convergence > 20:
            print('Model converged')
            break


def train_model(cfg):
    # select the appropriate model
    model_name = cfg['model_name']

    # hyperparameters
    seed = cfg['seed']
    batch_size = cfg['batch_size']
    epochs = cfg['epochs']
    dataset_path = cfg['dataset_path']
    learning_rate = cfg['learning_rate']

    # create sets from original folder if not yet present
    if not os.path.exists('sets'):
        create_sets(dataset_path)

    num_classes = len(os.listdir(os.path.join('sets', 'training')))

    # check if model directory is present
    if not os.path.exists(os.path.join('models', model_name)):
        os.makedirs(os.path.join('models', model_name))
        os.makedirs(os.path.join('models', model_name, 'performance'))

    # check if cuda is available and set device along with cuda seed
    device = get_device(seed)

    # set torch seed for reproducibility
    torch.manual_seed(seed)

    # parameters for early stopping
    best_loss = 999999
    convergence = 0

    # logging of diverse performance
    train_losses = []
    train_accuracies = []
    train_f1_scores = []
    val_losses = []
    val_accuracies = []
    val_f1_scores = []

    # pretrain the model on CIFAR-10
    if cfg['pretrain_CIFAR']:
        model, shape = get_model(model_name, cfg['pretrained_weights'], cfg['finetune_layer'], cfg['pretrained_model'],
                                 10, cfg['layers'])
        model.to(device)
        train_on_cifar(model_name, model, shape, device)
        model.load_state_dict(torch.load(os.path.join('models', model_name, f'{model_name}.pkl')))
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    else:
        model, shape = get_model(model_name, cfg['pretrained_weights'], cfg['finetune_layer'], cfg['pretrained_model'],
                                 num_classes, cfg['layers'])
        model.to(device)

    # dataset and augmentation
    transforms_list = [transforms.Resize(shape)]

    if cfg['fliplr']:   # horizontal flip
        transforms_list.append(transforms.RandomHorizontalFlip())
    if cfg['gaussian_blur']:    # Gaussian blur
        transforms_list.append(transforms.GaussianBlur(cfg['gaussian_kernel'], (cfg['sigma_min'], cfg['sigma_max'])))
    if cfg['affine']:    # affine
        transforms_list.append(transforms.RandomAffine(cfg['affine_percent'], scale=(cfg['affine_scale_min'], cfg['affine_scale_max'])))
    if cfg['jitter']:
        transforms_list.append(
            transforms.ColorJitter(brightness=(cfg['jitter_min'], cfg['jitter_max']),
                                   contrast=(cfg['jitter_min'], cfg['jitter_max']),
                                   hue=cfg['jitter_hue'],
                                   saturation=(cfg['jitter_min'], cfg['jitter_max'])))

    transforms_list.append(transforms.ToTensor())
    transforms_list.append(transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]))
    transform = transforms.Compose(transforms_list)

    val_transform = transforms.Compose([
            transforms.Resize(shape),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    train_loader = create_dataloader(os.path.join('sets', 'training'), transform, batch_size)
    val_loader = create_dataloader(os.path.join('sets', 'validation'), val_transform, batch_size)

    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, amsgrad=True)

    if cfg['optimizer_scheduler']:
        scheduler = ReduceLROnPlateau(optimizer, 'min', factor=cfg['scheduler_gamma'],
                                      patience=cfg['scheduler_patience'], threshold=cfg['scheduler_threshold'],
                                      threshold_mode='rel', verbose=True)
    else:
        scheduler = None

    criterion = nn.CrossEntropyLoss()
    model.to(device)

    for epoch in range(0, epochs):
        print(f'Epoch: {epoch}')
        train_loss, train_acc, train_f1 = train(
            train_loader,
            model,
            optimizer,
            criterion,
            device
        )
        val_loss, val_acc, val_f1, _ = test(val_loader, model, criterion, device)

        if scheduler is not None:
            scheduler.step(val_loss)
        # logging losses
        train_losses.append(train_loss)
        train_accuracies.append(train_acc)
        train_f1_scores.append(train_f1)
        val_losses.append(val_loss)
        val_accuracies.append(val_acc)
        val_f1_scores.append(val_f1)

        if val_loss <= best_loss:
            best_loss = val_loss
            print('Saving model')
            torch.save(model.state_dict(), os.path.join('models', model_name, f'{model_name}.pkl'))
            convergence = 0
        else:
            convergence += 1

        if convergence > cfg['convergence']:
            print('Model converged')
            break

    np.save(os.path.join('models', model_name, 'performance', 'train_losses.npy'), train_losses)
    np.save(os.path.join('models', model_name, 'performance', 'train_accuracies.npy'), train_accuracies)
    np.save(os.path.join('models', model_name, 'performance', 'train_f1_scores.npy'), train_f1_scores)
    np.save(os.path.join('models', model_name, 'performance', 'val_losses.npy'), val_losses)
    np.save(os.path.join('models', model_name, 'performance', 'val_accuracies.npy'), val_accuracies)
    np.save(os.path.join('models', model_name, 'performance', 'val_f1_scores.npy'), val_f1_scores)


def test2(test_loader, model, criterion, device):
    model.eval()
    test_loss = 0.0
    true_labels = []
    predicted_labels = []
    total = 0

    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            test_loss += loss.item() * images.size(0)
            _, preds = torch.max(outputs.data, 1)
            true_labels.extend(labels.cpu().numpy())
            predicted_labels.extend(preds.cpu().numpy())
            total += labels.size(0)

    test_loss /= len(test_loader.dataset)
    test_acc = Decimal(sum([1 for i, j in zip(true_labels, predicted_labels) if i == j])) / Decimal(total)
    miss_classified = sum([1 for i, j in zip(true_labels, predicted_labels) if i != j])
    test_f1 = f1_score(true_labels, predicted_labels, average='macro')
    test_precision = precision_score(true_labels, predicted_labels, average='macro')
    test_recall = recall_score(true_labels, predicted_labels, average='macro')
    conf_matrix = confusion_matrix(true_labels, predicted_labels)

    print('Test loss: {:.3f}, Test accuracy: {:.3f}, Test Macro F1-score: {:.3f}'.format(test_loss, test_acc, test_f1))

    return test_loss, test_acc, test_f1, conf_matrix, miss_classified, test_precision, test_recall


def test_model(cfg):
    model_name = cfg['model_name']
    num_classes = len(os.listdir(os.path.join('sets', 'test')))
    model, shape = get_model(model_name, cfg['pretrained_weights'], cfg['finetune_layer'], cfg['pretrained_model'],
                             num_classes, cfg['layers'])
    device = get_device(cfg['seed'])

    model.to(device)
    model.eval()

    # add to increase the dataset size
    """for folder in os.listdir(os.path.join('sets', 'test')):
        for image in os.listdir(os.path.join('sets', 'test', folder)):
            for i in range(9):
                shutil.copy(os.path.join('sets', 'test', folder, image), os.path.join('sets', 'test', folder, image[:-4] + f'_{i}.jpg'))"""

    """transform = transforms.Compose([
        transforms.Resize(shape),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])"""
    transforms_list = [transforms.Resize(shape)]

    if cfg['fliplr']:  # horizontal flip
        transforms_list.append(transforms.RandomHorizontalFlip())
    if cfg['gaussian_blur']:  # Gaussian blur
        transforms_list.append(transforms.GaussianBlur(cfg['gaussian_kernel'], (cfg['sigma_min'], cfg['sigma_max'])))
    if cfg['affine']:  # affine
        transforms_list.append(
            transforms.RandomAffine(cfg['affine_percent'], scale=(cfg['affine_scale_min'], cfg['affine_scale_max'])))
    if cfg['jitter']:
        transforms_list.append(
            transforms.ColorJitter(brightness=(cfg['jitter_min'], cfg['jitter_max']),
                                   contrast=(cfg['jitter_min'], cfg['jitter_max']),
                                   hue=cfg['jitter_hue'],
                                   saturation=(cfg['jitter_min'], cfg['jitter_max'])))

    transforms_list.append(transforms.ToTensor())
    transforms_list.append(transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]))
    transform = transforms.Compose(transforms_list)

    test_loader = create_dataloader(os.path.join('sets', 'test'), transform, 64)
    criterion = nn.CrossEntropyLoss()

    test_loss, test_acc, test_f1, conf_matrix, miss_classified, test_precision, test_recall = test2(test_loader, model, criterion, device)
    with open(os.path.join('models', model_name, 'performance', 'test_results.txt'), 'w') as f:
        f.write('Test loss: {:.3f}, Test accuracy: {:.3f}, Test Macro F1-score: {:.3f}, Precision {:.3f}, Recall {:.3f}, Badly classified: {}'
                .format(test_loss, test_acc, test_f1, test_precision, test_recall, miss_classified))

    df_cm = pd.DataFrame(conf_matrix, index=[i for i in os.listdir(os.path.join('sets', 'training'))],
                         columns=[i for i in os.listdir(os.path.join('sets', 'training'))])
    plt.figure(figsize=(10, 10))
    sn.heatmap(df_cm, annot=True)
    plt.savefig(os.path.join('models', model_name, 'performance', 'confusion_matrix.png'))
    #folder_to_zip(os.path.join('models', model_name, 'performance'))
