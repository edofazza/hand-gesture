import os
import numpy as np
import matplotlib.pyplot as plt


def zip_to_folder(zip_path: str = 'models/resnet-fc-18/performance.zip') -> str:
    os.system(f'unzip {zip_path}')
    return 'models/resnet-fc-18/performance'


def folder_to_zip(folder_path: str = 'models/resnet-fc-18/performance') -> bool:
    return os.system(f'zip -r {folder_path}.zip {folder_path}') == 0


def plot(performance_folder: str = 'models/resnet-fc-18/performance', num: int = 1) -> None:
    if num == 1:
        train = np.load(os.path.join(performance_folder, 'train_losses.npy'))
        val = np.load(os.path.join(performance_folder, 'val_losses.npy'))
    elif num == 2:
        train = np.load(os.path.join(performance_folder, 'train_accuracies.npy'))
        val = np.load(os.path.join(performance_folder, 'val_accuracies.npy'))
    else:
        train = np.load(os.path.join(performance_folder, 'train_f1_scores.npy'))
        val = np.load(os.path.join(performance_folder, 'val_f1_scores.npy'))

    epochs = len(train)
    plt.plot(np.arange(epochs), train, 'b', label='Training accuracy')
    plt.plot(np.arange(epochs), val, 'g', label='Validation accuracy')

    if num == 1:
        plt.title('Training and validation losses')
        plt.legend(loc='upper right')
        plt.savefig(os.path.join(performance_folder, 'loss_plot.png'))
    elif num == 2:
        plt.title('Training and validation accuracies')
        plt.legend(loc='lower right')
        plt.savefig(os.path.join(performance_folder, 'accuracy_plot.png'))
    else:
        plt.title('Training and validation F1 accuracies')
        plt.legend(loc='lower right')
        plt.savefig(os.path.join(performance_folder, 'F1_score_plot.png'))


def read_test_best() -> tuple:
    with open('models/resnet-fc-18/performance/test_results.txt', 'r') as f:
        loss, acc, f1 = [e[-5:] for e in f.readline().split(',')]
    return loss, acc, f1


def prepare_data_for_gui_zip(zip_path: str = 'models/resnet-fc-18/performance.zip') -> tuple:
    performance_folder = zip_to_folder(zip_path)
    plot(performance_folder, 1)
    plot(performance_folder, 2)
    plot(performance_folder, 3)
    test_loss, test_acc, test_f1 = read_test_best()
    return os.path.join(performance_folder, 'accuracy_plot.png'), os.path.join(performance_folder, 'loss_plot.png'), os.path.join(performance_folder, 'F1_score_plot.png'), \
           test_loss, test_acc, test_f1


def prepare_data_for_gui(performance_folder: str = 'models/resnet-fc-18/performance/') -> tuple:
    plot(performance_folder, True)
    plot(performance_folder, False)
    test_loss, test_acc, test_f1 = read_test_best()
    return os.path.join(performance_folder, 'accuracy_plot.png'), os.path.join(performance_folder, 'loss_plot.png'),\
           test_loss, test_acc, test_f1
