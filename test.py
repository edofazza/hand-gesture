import os

from code.training.train_model import train_model, test_model
from code.utils.configuration import create_configuration_file, load_configuration_file

if __name__ == '__main__':
    os.environ['TORCH_HOME'] = './cache'
    #create_configuration_file()
    cfg = load_configuration_file('config.yaml')
    #train_model(cfg)
    cfg['pretrained_weights'] = False
    cfg['pretrained_model'] = True
    test_model(cfg)
