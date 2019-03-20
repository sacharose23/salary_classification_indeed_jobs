### This script opens our Indeed Job Post dataset and 
### fits a logistic regression model that takes in our basic features
### and classifies each 

### Import the libraries
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def logisticmodel_matrixinput():
    ### Import pickle & load dictionary from pickle (test set is not included)
    ### data is a list of dictionary elements
    data = pickle.load( open("data_2.2.pkl", "rb") )

    ## Separating features from labels
    data = np.asarray(data)
    length = data.shape[1]

    # pull out years_experience
    title_location = data[:,0:2]
    technologies = data[:,3:-1]

    y = data[:,-1]
    X = np.concatenate((title_location, technologies), axis=1)

    ### Splitting dataset into train:test:val sets via 70:20:10 ratio
    # Split dataset into training/testing and validation sets
    from sklearn.model_selection import train_test_split
    X_tt, X_val, y_tt, y_val = train_test_split(X, y, test_size = 0.10, random_state = 0)
    pd.DataFrame(X_val).to_csv("data_2.2_val_features.csv")
    pd.DataFrame(y_val).to_csv("data_2.2_val_labels.csv")
    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_tt, y_tt, test_size = 0.20/0.90, random_state = 0)
    pd.DataFrame(y_test).to_csv("data_2.2_test_labels.csv")

    # Fitting Logistic Regression to the Training set
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import OneHotEncoder
    enc = OneHotEncoder(handle_unknown='ignore')
    enc.fit(X_train)
    X_train_one_hot = enc.transform(X_train)
    X_test_one_hot = enc.transform(X_test)
    y_train=y_train.astype('int')
    classifier = LogisticRegression(solver='lbfgs')
    
    classifier.fit(X_train_one_hot, y_train)

    # Find predictions for validation set
    y_test_pred = classifier.predict(X_test_one_hot)
    pd.DataFrame(y_test_pred).to_csv("data_2.2_test_pred.csv") 

    return (y_test, y_test_pred)