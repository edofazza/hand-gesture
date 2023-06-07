import os

from code.training.train_model import train_model, test_model
from code.utils.configuration import create_configuration_file, load_configuration_file

if __name__ == '__main__':
    os.environ['TORCH_HOME'] = './cache'

    create_configuration_file(model_name='custom_resnet_3_3_3', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    train_model(cfg)
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='custom_densenet_3_3_3', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    train_model(cfg)
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='custom_senet_3_3_3', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    train_model(cfg)
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='custom_resnet_3_3_3_cifar', pretrained_weights=False, pretrain_CIFAR=True)
    cfg = load_configuration_file('config.yaml')
    train_model(cfg)
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='custom_densenet_3_3_3_cifar', pretrained_weights=False, pretrain_CIFAR=True)
    cfg = load_configuration_file('config.yaml')
    train_model(cfg)
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='custom_senet_3_3_3_cifar', pretrained_weights=False, pretrain_CIFAR=True)
    cfg = load_configuration_file('config.yaml')
    train_model(cfg)
    cfg['pretrained_model'] = True
    test_model(cfg)
    