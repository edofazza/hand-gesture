import yaml

dictionary = {
    # MODEL PARAMETERS
    'model_name': 'resnet-50',
    'pretrained_weights': True,  # imagenet or not
    'finetune_layer': 'fc',
    'pretrain_CIFAR': False,
    'pretrained_model': False,
    'layers': [3, 3, 3],
    # TRAINING PARAMETERS
    'batch_size': 1024,
    'epochs': 1000,
    'dataset_path': 'hand_gestures',
    'learning_rate': 0.001,
    'optimizer_scheduler': True,
    'scheduler_gamma': 0.2,
    'scheduler_patience': 100,
    'scheduler_threshold': 1e-4,
    'convergence': 50,
    # DATA AUGMENTATION PARAMETERS
    'fliplr': True,
    'fliplr_value': 0.5,
    'gaussian_blur': True,
    'sigma_min': 0,
    'sigma_max': 1.0,
    'linear_contrast': True,
    'lc_min': 0.8,
    'lc_max': 1.2,
    'affine': True,
    'affine_percent': 10,
    'affine_scale_min': 0.8,
    'affine_scale_max': 1.2,
    'jitter': True,
    'jitter_min': 0.8,
    'jitter_max': 1.2,
    # GENERAL
    'seed': 42,
}


def create_configuration_file():
    with open('config.yaml', 'wb') as f:
        yaml.dump(dictionary, f)


def load_configuration_file(config_path):
    with open(config_path, 'rb') as f:
        cfg = yaml.safe_load(f)
    return cfg

