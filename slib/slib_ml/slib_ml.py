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