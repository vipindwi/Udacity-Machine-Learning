#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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



#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score


clf = svm.SVC(kernel='rbf',C=10000.0)


t0 = time()
clf.fit(features_train, labels_train)
print 'Training Time ', round(time()-t0, 3), "s"

t1 = time()
prediction = clf.predict(features_test)
print 'Prediction Time ', round(time()-t1, 3), "s"


print 'The predictions for 10th ', prediction[10]
print 'The predictions for 26th ', prediction[26]
print 'The predictions for 50th ', prediction[50]

count = 0
for x in prediction:
	if x == 1:
		count = count + 1

print 'The count is ',count

score = accuracy_score(labels_test,prediction)
print 'The score is ', score


#########################################################


