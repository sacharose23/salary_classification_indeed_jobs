### This script opens our Indeed Job Post dataset and 
### fits a logistic regression model that takes in our basic features
### and classifies each 

### Import the libraries
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def logisticmodel():
    ### Import pickle & load dictionary from pickle (test set is not included)
    ### data is a list of dictionary elements
    data = pickle.load( open("data_basic.pkl", "rb") )

    # remove empty dictionaries
    while {} in data:
        data.remove({})

    ### Change dictionary into matrix form
    data_length = len(data)
    orderedKeyValues = ['job_title','city','salary_range'] #list of columns/features we'd like to remove
    dataArrays = []
    # loop through the list of dict and create an array for each dict. element.
    # append the arrays together
    for d in range(data_length):
        dic = data[d]
        dataArray = np.array([dic[i] for i in orderedKeyValues])
        dataArrays.append(dataArray)

    data = np.stack(dataArrays, axis = 0)
    # data.shape 
    # 14867 posts with 2 features and 1 label

    ## Separating features from labels
    job_titles = [job_title[0] for job_title in data]
    cities = [city[1] for city in data]
    X = []
    X.append(job_titles)
    X.append(cities)
    X = np.asarray(X)
    X = np.transpose(X)
    X.shape
    y = [salary_range[2] for salary_range in data]
    y = np.asarray(y)

    ### Splitting dataset into train:test:val sets via 70:20:10 ratio
    # Split dataset into training/testing and validation sets
    from sklearn.model_selection import train_test_split
    X_tt, X_val, y_tt, y_val = train_test_split(X, y, test_size = 0.10, random_state = 0)
    pd.DataFrame(X_val).to_csv("data_basic_val_features.csv")
    pd.DataFrame(y_val).to_csv("data_basic_val_labels.csv")
    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_tt, y_tt, test_size = 0.20/0.90, random_state = 0)
    pd.DataFrame(y_test).to_csv("data_basic_test_labels.csv")

    # Fitting Logistic Regression to the Training set
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import OneHotEncoder
    enc = OneHotEncoder(handle_unknown='ignore')
    enc.fit(X_train)
    X_train_one_hot = enc.transform(X_train)
    X_test_one_hot = enc.transform(X_test)
    classifier = LogisticRegression()
    classifier.fit(X_train_one_hot, y_train)

    # Find predictions for validation set
    y_test_pred = classifier.predict(X_test_one_hot)
    pd.DataFrame(y_test_pred).to_csv("data_basic_test_pred.csv") 

    return (y_test, y_test_pred)