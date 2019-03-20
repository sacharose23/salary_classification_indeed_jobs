import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix

def evaluations(y_test, y_pred):

    # Change type to floats
    y_pred = y_pred.astype('float')
    y_test = y_test.astype('float')

    ### Evaluating the Model using the Testing Dataset
    # Plot normalized confusion matrix
    labels = ['50-60', '60-70', '70-80', '80-90', '90-100', '100-110', '110-120', '120-130', '130-140', '140-150', '150-160', '160-170', '170+']
    from plot_conf_matrix import plot_confusion_matrix

    # Compute confusion matrix
    cnf_matrix = confusion_matrix(y_test, y_pred)
    np.set_printoptions(precision=2)

    # Plot normalized confusion matrix
    # Plot normalized confusion matrix
    fig, ax = plt.subplots( nrows=1, ncols=1 , figsize=(8, 8)) 
    plot_confusion_matrix(cnf_matrix, normalize = True, classes=labels, title='Normalized Confusion Matrix')
    fig.savefig('norm_conf_matrix.png')
    plt.close(fig)
    
    # extracting true positives, false negatives, and false positives
    cm = confusion_matrix(y_test, y_pred)
    cm = np.asmatrix(cm)
    tp = np.trace(cm)
    fn = np.triu(cm).sum()-np.trace(cm)
    fp = np.tril(cm).sum()-np.trace(cm)

    # Precision (if we want to minimize false positives)
    precision = tp / (tp + fp)
    print("Precision {:0.2f}".format(precision))

    # Recall (least false negatives)
    recall = tp / (tp + fn)
    print("Recall {:0.2f}".format(recall))

    # F1 Score
    # Harmonic mean of PR, used to indicate a balance between 
    # PR providing each equal weightage, it ranges from 0 to 1. 
    # F1 Score reaches its best value at 1 (perfect PR) and worst at 0.
    # Relations between data’s positive labels and those given by a classifier based on sums of per-text decisions
    f1 = (2*precision*recall)/(precision + recall)
    print("F1 Score {:0.2f}".format(f1))

    ### Calculate RSME
    from sklearn.metrics import mean_squared_error
    from math import sqrt
    rmse = sqrt(mean_squared_error(y_test.astype(np.float), y_pred.astype(np.float)))
    print("RMSE {:0.2f}".format(rmse))

# ------------------------------------------
# Plot a Confusion Matrix 
# from sklearn.metrics import confusion_matrix
# import seaborn as sn
# cm = confusion_matrix(y_val,y_pred)
# cm_df = pd.DataFrame(cm)
# plt.figure(figsize = (10,7))
# sn.heatmap(cm_df, annot=True)