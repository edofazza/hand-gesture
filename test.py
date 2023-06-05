from code.training.train_model import train_model, test_model
from code.utils.configuration import create_configuration_file, load_configuration_file

if __name__ == '__main__':
    create_configuration_file()
    cfg = load_configuration_file('config.yaml')
    train_model(cfg)
    test_model(cfg)
    