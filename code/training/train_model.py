import os
import torch
import torchvision.datasets
from torch.utils import data
from torchvision import transforms
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch import nn
import imgaug.augmenters as iaa
from sklearn.metrics import f1_score
import numpy as np


from code.training.models import get_model
from code.training.auxiliary import create_sets, create_dataloader, get_device


def train(train_loader, model, optimizer, scheduler, criterion, device):
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

    if scheduler is not None:
        scheduler.step()

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

    print('Test loss: {:.3f}, Test accuracy: {:.3f}, Test Macro F1-score: {:.3f}'.format(test_loss, test_acc, test_f1))

    return test_loss, test_acc, test_f1


def train_on_mnist(model_name, model, shape, device):
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

    train_dataset = torchvision.datasets.CIFAR10(root='.', train=True, transform=transform_train)
    test_dataset = torchvision.datasets.CIFAR10(root='.', train=False, transform=transform_test)

    train_loader = data.DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = data.DataLoader(test_dataset, batch_size=64, shuffle=False)

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
            None,
            criterion,
            device
        )
        test_loss, _, _ = test(test_loader, model, criterion, device)

        if test_loss <= best_loss:
            best_loss = test_loss
            print('Saving model')
            torch.save(model.state_dict(), os.path.join('models', model_name, f'{model_name},pkl'))
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
        os.makedirs(os.path.join('models', model_name, 'losses'))

    # check if cuda is available and set device along with cuda seed
    device = get_device(seed)

    # set torch seed for reproducibility
    torch.manual_seed(seed)

    # parameters for early stopping
    best_loss = 999999
    convergence = 0

    # logging of diverse losses
    train_losses = []
    train_accuracies = []
    train_f1_scores = []
    val_losses = []
    val_accuracies = []
    val_f1_scores = []

    # pretrain the model on CIFAR-10
    if cfg['pretrain_CIFAR']:
        model, shape = get_model(model_name, cfg['pretrained_weights'], cfg['finetune_layer'], cfg['pretrained_model'],
                                 10)
        model.to(device)
        train_on_mnist(model_name, model, shape, device)
        model.load_state_dict(torch.load(os.path.join('model', model_name, f'{model_name}.pkl')))
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    else:
        model, shape = get_model(model_name, cfg['pretrained_weights'], cfg['finetune_layer'], cfg['pretrained_model'],
                                 num_classes)
        model.to(device)

    # dataset and augmentation
    augmenters_list = []

    if cfg['fliplr']:   # horizontal flip
        augmenters_list.append(iaa.Fliplr(cfg['fliplr_value']))
    if cfg['guassian_blur']:    # Gaussian blur
        augmenters_list.append(iaa.GaussianBlur(sigma=(cfg['sigma_min'], cfg['sigma_max'])))
    if cfg['linear_contrast']:    # linear contrast
        augmenters_list.append(iaa.LinearContrast((cfg['lc_min'], cfg['lc_max'])))
    if cfg['affine']:    # affine
        augmenters_list.append(iaa.Affine(
            rotate=(-cfg['affine_percent'], cfg['affine_percent']),
            translate_percent={"x": (-cfg['affine_percent'], cfg['affine_percent']), "y": (-cfg['affine_percent'], cfg['affine_percent'])},
            scale=(cfg['affine_scale_min'], cfg['affine_scale_max'])
        ))
    if cfg['jitter']:
        augmenters_list.append(
            iaa.SomeOf((0, 3), [
                iaa.MultiplyBrightness((cfg['jitter_min'], cfg['jitter_max'])),  # brightness
                iaa.ContrastNormalization((cfg['jitter_min'], cfg['jitter_max'])),  # contrast
                iaa.MultiplyHueAndSaturation((cfg['jitter_min'], cfg['jitter_max']))  # hue and saturation
            ])
        )

    if augmenters_list:
        augmenter = iaa.Sequential([
            augmenters_list
        ])

        transform = transforms.Compose([
            transforms.Resize(shape),
            transforms.Lambda(lambda x: augmenter(x)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
    else:
        transform = transforms.Compose([
            transforms.Resize(shape),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
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

    for epoch in range(0, epochs):
        print(f'Epoch: {epoch}')
        train_loss, train_acc, train_f1 = train(
            train_loader,
            model,
            optimizer,
            scheduler,
            criterion,
            device
        )
        val_loss, val_acc, val_f1 = test(val_loader, model, criterion, device)

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
            torch.save(model.state_dict(), os.path.join('models', model_name, f'{model_name},pkl'))
            convergence = 0
        else:
            convergence += 1

        if convergence > cfg['convergence']:
            print('Model converged')
            break

    np.save(os.path.join('models', model_name, 'losses', 'val_losses.npy'), train_losses)
    np.save(os.path.join('models', model_name, 'losses', 'val_accuracies.npy'), train_accuracies)
    np.save(os.path.join('models', model_name, 'losses', 'val_f1_scores.npy'), train_f1_scores)
    np.save(os.path.join('models', model_name, 'losses', 'val_losses.npy'), val_losses)
    np.save(os.path.join('models', model_name, 'losses', 'val_accuracies.npy'), val_accuracies)
    np.save(os.path.join('models', model_name, 'losses', 'val_f1_scores.npy'), val_f1_scores)


def test_model(cfg):
    model_name = cfg['model_name']
    num_classes = os.listdir(os.path.join('sets', 'training'))
    model, shape = get_model(model_name, cfg['pretrained_weights'], cfg['finetune_layer'], cfg['pretrained_model'], num_classes)
    device = get_device(cfg['seed'])

    if os.path.exists(os.path.join('models', model_name, f'{model_name}.pkl')):
        model.load_state_dict(torch.load(os.path.join('models', model_name, f'{model_name}.pkl')))
    else:
        print(f'Model {model_name} not present')
        return

    model.to(device)
    model.eval()

    transform = transforms.Compose([
        transforms.Resize(shape),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    test_loader = create_dataloader(os.path.join('sets', 'validation'), transform, cfg['batch_size'])
    criterion = nn.CrossEntropyLoss()

    test_loss, test_acc, test_f1 = test(test_loader, model, criterion, device)
    with open(os.path.join('models', model_name, 'test_results.txt'), 'w') as f:
        f.write('Test loss: {:.3f}, Test accuracy: {:.3f}, Test Macro F1-score: {:.3f}'.format(test_loss, test_acc, test_f1))
