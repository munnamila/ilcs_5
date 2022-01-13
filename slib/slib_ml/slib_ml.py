import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns

def test():
    print('OK')

def confusion_matrix(list_labels, list_predictions):
    cm = confusion_matrix(list_labels, list_predictions)
    fig = plt.figure()
    sns_plot = sns.heatmap(cm, annot=True, cmap='Greys')
    plt.title('test')
    plt.xlabel('prediction')
    plt.ylabel('truth')
    plt.show()

def print_training_info(train_accuracy, train_loss, test_accuracy, test_loss):
    print('train_accuracy: %.05f train_loss: %.05f test_accuracy: %.05f test_loss: %.05f' % (train_accuracy, train_loss, test_accuracy, test_loss))

def print_graph_info(train_accuracy_list, train_loss_list, test_accuracy_list, test_loss_list):

    plt.plot(range(len(train_loss_list)), train_loss_list, label='list_train_loss')
    plt.plot(range(len(test_loss_list)), test_loss_list, label='list_test_loss')
    plt.grid(True)
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.legend(bbox_to_anchor=(1,1), loc='center left')
    plt.show()

    plt.plot(range(len(train_accuracy_list)), train_accuracy_list, label='train_accuracy')
    plt.plot(range(len(test_accuracy_list)), test_accuracy_list, label='test_accuracy')
    plt.grid(True)
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.legend(bbox_to_anchor=(1,1), loc='center left')
    plt.show()


