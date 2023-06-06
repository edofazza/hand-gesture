import torch
from torch import nn
from torchvision.models import resnet18, resnet50, resnet101, densenet121, vgg16, inception_v3, efficientnet_b0
import os

from code.training.custom_models import CustomResNet, CustomDenseNet, CustomSEResNet, BasicBlock


def get_resnet(model_name, pretrained_weights=False):
    model = None
    if model_name.endswith('18'):
        if pretrained_weights:
            model = resnet18(weights='IMAGENET1K_V1')
        else:
            model = resnet18()
    elif model_name.endswith('50'):
        if pretrained_weights:
            model = resnet50(weights='IMAGENET1K_V1')
        else:
            model = resnet50()
    elif model_name.endswith('101'):
        if pretrained_weights:
            model = resnet101(weights='IMAGENET1K_V1')
        else:
            model = resnet101()
    else:
        print('ResNet model selected not present, try 18, 50, 101')

    return model


def get_densenet(model_name, pretrained_weights=False):
    model = None
    if model_name.endswith('121'):
        if pretrained_weights:
            model = densenet121(weights='IMAGENET1K_V1')
        else:
            model = densenet121()
    else:
        print('DenseNet model selected not present, try 121')
    return model


def get_vgg(model_name, pretrained_weights=False):
    model = None
    if model_name.endswith('16'):
        if pretrained_weights:
            model = vgg16(weights='IMAGENET1K_V1')
        else:
            model = vgg16()
    else:
        print('Vgg model selected not present, try 16')
    return model


def get_inception(model_name, pretrained_weights=False):
    model = None
    if model_name.endswith('b0'):
        if pretrained_weights:
            model = efficientnet_b0(weights='IMAGENET1K_V1')
        else:
            model = efficientnet_b0()
    else:
        print('EfficientNet model selected not present, try EfficientNet_b0')
    return model


def get_efficientnet(model_name, pretrained_weights=False):
    model = None
    if model_name.endswith('v3'):
        if pretrained_weights:
            model = inception_v3(weights='IMAGENET1K_V1')
        else:
            model = inception_v3()
    else:
        print('Inception model selected not present, try inception_v3')
    return model


def get_model(model_name: str, pretrained_weights, finetune_layer, pretrained_model, num_classes,
              layers=None, growth_rate=32):
    if model_name.startswith('resnet'):
        model = get_resnet(model_name, pretrained_weights)
        shape = (224, 224)
    elif model_name.startswith('densenet'):
        model = get_densenet(model_name, pretrained_weights)
        shape = (224, 224)
    elif model_name.startswith('vgg'):
        model = get_vgg(model_name, pretrained_weights)
        shape = (224, 224)
    elif model_name.startswith('inception'):
        model = get_inception(model_name, pretrained_weights)
        shape = (299, 299)
    elif model_name.startswith('efficientnet'):
        model = get_efficientnet(model_name, pretrained_weights)
        shape = (224, 224)
    elif model_name.startswith('custom_resnet'):
        model = CustomResNet(num_classes, layers)
        shape = (50, 50)
    elif model_name.startswith('custom_densenet'):
        model = CustomDenseNet(num_classes, growth_rate, layers)
        shape = (50, 50)
    elif model_name.startswith('custom_senet'):
        model = CustomSEResNet(BasicBlock, layers, num_classes)
        shape = (50, 50)
    else:
        print('Error in model_name')
        return None

    if model is None:
        print('Model is None')
        return None

    model.fc = nn.Linear(model.fc.in_features, num_classes)

    if pretrained_weights:
        found_start_layer = False
        for name, param in model.named_parameters():
            if finetune_layer in name:
                found_start_layer = True
            if found_start_layer:
                param.requires_grad = True
            else:
                param.requires_grad = False

    if pretrained_model:
        if os.path.exists(os.path.join('model', model_name, f'{model_name}.pkl')):
            model.load_state_dict(torch.load(os.path.join('model', model_name, f'{model_name}.pkl')))
            print('Weights loaded')
        else:
            print('Error in loading weights')
    return model, shape


def get_model_layers(model_name):
    if model_name.startswith('resnet'):
        model = get_resnet(model_name)
    elif model_name.startswith('densenet'):
        model = get_densenet(model_name)
    elif model_name.startswith('vgg'):
        model = get_vgg(model_name)
    elif model_name.startswith('inception'):
        model = get_inception(model_name)
    elif model_name.startswith('efficientnet'):
        model = get_efficientnet(model_name)
    else:
        print('Error in model_name')
        return None

    layers = []
    for name, _ in model.named_children():
        layers.append(name)
    return layers
