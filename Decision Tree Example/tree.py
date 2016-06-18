# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:29:26 2016

@author: akhan
"""

import numpy as np
from sklearn import svm


#Loading Data from CSV
import pandas as pd
data_pd = pd.read_csv('/home/akhan/Documents/data.csv',sep=';')

# The size of the dataset is store in 'n'
n = data_pd.shape[0]

## DATA CLEANING A FORMATING

# Dropping the 'name' column since it has no predictive power
data_pd = data_pd.drop('name',1)

# Replacing categorical variables with binary variables
dummies_col1 = pd.get_dummies(data_pd['col1'])    .drop('cat1',1)
dummies_col2 = pd.get_dummies(data_pd['col2'])       .drop('cat1',1)  
dummies_col3 = pd.get_dummies(data_pd['col3'])          .drop('cat1',1)
dummies_col4 = pd.get_dummies(data_pd['col4']).drop('cat1',1)
dummies_response  = pd.get_dummies(data_pd['response'])        .drop('no',1)
data_pd = data_pd.drop(['col1','col2','col2','col4','response'],1)
data_pd = pd.concat([data_pd, dummies_col1, dummies_col2, dummies_col3, dummies_col4, dummies_response], ignore_index=False, axis =1)
Y = data_pd['yes']       .as_matrix()
X = data_pd.drop('yes',1).as_matrix()

## END OF DATA CLEANING



from sklearn import tree

## Decision Tree 
from sklearn import metrics
from sklearn.cross_validation import KFold
kf = KFold(n,5,shuffle=True)
error = 0

for train_idx, test_idx in kf:
    #print "Train:",train_idx,"Test:",test_idx
    X_train, X_test, Y_train, Y_test = X[train_idx], X[test_idx], Y[train_idx], Y[test_idx]
    clf = tree.DecisionTreeClassifier()
    clif = clf.fit(X_train,Y_train)
    Y_hat=clf.predict(X_test)
    cMatrix = metrics.confusion_matrix(Y_test,Y_hat)
    error = error + (cMatrix[0][1]+cMatrix[1][0]) * 100/ sum(sum(cMatrix))

avgError = error/len(kf)
print "5-Fold Cross Validation Error is ", "".join([str(avgError),"%"])



## Decision Tree : (Same as above just consise code)
from sklearn.cross_validation import cross_val_score
clf = tree.DecisionTreeClassifier()
avgError = (1 - np.mean(cross_val_score(clf, X, Y, cv = 5))) *100
print "5-Fold Cross Validation Error is ", "".join([str(avgError),"%"])
