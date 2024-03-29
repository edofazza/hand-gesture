import os

from code.training.train_model import train_model, test_model
from code.utils.configuration import create_configuration_file, load_configuration_file
from code.training.auxiliary import create_sets

if __name__ == '__main__':
    os.environ['TORCH_HOME'] = './cache'

    create_sets('hand_gestures')

    create_configuration_file(model_name='resnet-fc-101', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='resnet-fc-50', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='resnet-fc-18', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='resnet-scratch-101', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='resnet-scratch-50', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='resnet-scratch-18', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='vgg-scratch-16', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='vgg-classifier-16', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='densenet-classifier-121', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='densenet-scratch-121', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='densenet-classifier-121', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='efficientnet_scratch_b0', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='efficientnet_classifier_b0', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='inception_scratch_v3', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='inception_fc_v3', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='custom_densenet_3_3_3', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='custom_densenet_3_3_3_cifar', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='custom_resnet_3_3_3', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='custom_resnet_3_3_3_cifar', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='custom_senet_3_3_3', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)

    create_configuration_file(model_name='custom_senet_3_3_3_cifar', pretrained_weights=False)
    cfg = load_configuration_file('config.yaml')
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)
