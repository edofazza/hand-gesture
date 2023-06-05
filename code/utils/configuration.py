import yaml


def create_configuration_file(
        model_name='resnet-fc-50',
        pretrained_weights=True,
        finetune_layer='fc',
        pretrain_CIFAR=False,
        pretrained_model=False,
        layers=[3, 3, 3],
        growth_rate=32,
        # TRAINING PARAMETERS
        batch_size= 1024,
        epochs=1000,
        dataset_path='hand_gestures',
        learning_rate=0.001,
        optimizer_scheduler=True,
        scheduler_gamma=0.2,
        scheduler_patience=100,
        scheduler_threshold=1e-4,
        convergence=50,
        # DATA AUGMENTATION PARAMETERS
        fliplr=True,
        fliplr_value=0.5,
        gaussian_blur=True,
        gaussian_kernel=3,
        sigma_min=0.1,
        sigma_max=1.0,
        affine=True,
        affine_percent=10,
        affine_scale_min=0.6,
        affine_scale_max=1.2,
        jitter=True,
        jitter_min=0.8,
        jitter_max=1.2,
        jitter_hue=0.2,
        # GENERAL
        seed=42,
):
    dictionary = {
        # MODEL PARAMETERS
        'model_name': model_name,
        'pretrained_weights': pretrained_weights,  # imagenet or not
        'finetune_layer': finetune_layer,
        'pretrain_CIFAR': pretrain_CIFAR,
        'pretrained_model': pretrained_model,
        'layers': layers,  # For layers (ResNet) block_config(DenseNet) [custom]
        'growth_rate': growth_rate,  # For growth_rate (DenseNet) [custom]
        # TRAINING PARAMETERS
        'batch_size': batch_size,
        'epochs': epochs,
        'dataset_path': dataset_path,
        'learning_rate': learning_rate,
        'optimizer_scheduler': optimizer_scheduler,
        'scheduler_gamma': scheduler_gamma,
        'scheduler_patience': scheduler_patience,
        'scheduler_threshold': scheduler_threshold,
        'convergence': convergence,
        # DATA AUGMENTATION PARAMETERS
        'fliplr': fliplr,
        'fliplr_value': fliplr_value,
        'gaussian_blur': gaussian_blur,
        'gaussian_kernel': gaussian_kernel,
        'sigma_min': sigma_min,
        'sigma_max': sigma_max,
        'affine': affine,
        'affine_percent': affine_percent,
        'affine_scale_min': affine_scale_min,
        'affine_scale_max': affine_scale_max,
        'jitter': jitter,
        'jitter_min': jitter_min,
        'jitter_max': jitter_max,
        'jitter_hue': jitter_hue,
        # GENERAL
        'seed': seed,
    }
    with open('config.yaml', 'wb') as f:
        yaml.dump(dictionary, f)


def load_configuration_file(config_path):
    with open(config_path, 'rb') as f:
        cfg = yaml.safe_load(f)
    return cfg

