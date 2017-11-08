#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

print 'The features_train ', features_train
print 'The  of features are ', features_train[0]
print 'the number of feature are ', len(features_train[0])



#########################################################
### your code goes here ###
from sklearn import tree
from sklearn.metrics import accuracy_score


classifier = tree.DecisionTreeClassifier(min_samples_split=40)
classifier.fit(features_train, labels_train)

prediction = classifier.predict(features_test)

accuracy = accuracy_score(labels_test, prediction)
print 'the accuracy is ', accuracy

#########################################################


