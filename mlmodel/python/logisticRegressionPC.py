
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn import preprocessing
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score

import sys
import os
import random
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.under_sampling import ClusterCentroids

def logreg():
    # data = np.loadtxt('featureneg.txt')
    # X = data[:,:5]
    # Y = data[:,5:].ravel()
    # X = preprocessing.scale(X)

    # data = np.loadtxt('oldfeature/featureneg01.txt')
    traindata = np.loadtxt('data/lgpc/train.txt')
    testdata = np.loadtxt('data/lgpc/test.txt')

    # truecount2 =  29579 # 32875
    # falsecount2 = 2814 # 3117
    FN = 1164

    X = traindata[:,:FN]
    Y = traindata[:,FN:].ravel()
    # print(sorted(Counter(Y).items()))
    # cc = ClusterCentroids(random_state=0)
    # X_r, y_r = cc.fit_resample(X, Y)
    # print(sorted(Counter(y_r).items()))

    from imblearn.under_sampling import RandomUnderSampler
    rus = RandomUnderSampler(random_state=0)
    X_r, y_r = rus.fit_resample(X, Y)
    # print(sorted(Counter(y_r).items()))
    # return
    min_max_scaler = preprocessing.MinMaxScaler()
    X1 = min_max_scaler.fit_transform(X_r)
    

    X_test = testdata[:,:FN]
    # min_max_scaler = preprocessing.MinMaxScaler()
    X_test = min_max_scaler.fit_transform(X_test)
    Y_test = testdata[:,FN:].ravel()

    # m,n = data.shape
    # print(X, Y)
    

    # print(truecount, falsecount)
    # print(type(data))

    # k = falsecount / truecount
    # mu = 0.5
    # print(k)
    # ccc = 0.0
    # f1macro = 0.0
    # f1micro = 0.0
    # kk  = 0.1

    # X_true_1, X_true_remain, Y_true_1, Y_true_remain = train_test_split(X_true, Y_true, test_size=1- k,random_state=random.randint(1, 100))

    # X1 = np.concatenate((X_true_1, X_false))
    # Y1 = np.append(Y_true_1, Y_false)

    # X_train, X_test, Y_train, Y_test = train_test_split(X1, Y1, test_size=kk, random_state=random.randint(1, 100))
    # print(X_train.shape[0])

    clf = LogisticRegression()
    clf.fit(X1,y_r)

    prediction = clf.predict(X_test)
    # y_prob = clf.predict_proba(X_test)
    # print(y_prob)
    accuracy = accuracy_score(Y_test, prediction)
    f1ma = f1_score(Y_test, prediction)
    f1mi = f1_score(Y_test, prediction, average='micro')
    print(precision_recall_fscore_support(Y_test, prediction))

    # prediction = clf.predict(X)
    # accuracy = accuracy_score(Y, prediction)
    # f1ma = f1_score(Y, prediction)
    # f1mi = f1_score(Y, prediction, average='micro')

    print('accuracy: ',  accuracy, "macro f1: ", f1ma, "micro f1: ", f1mi)
    # ccc += accuracy
    # f1macro += f1ma
    # f1micro += f1mi
    # print("average score: ", ccc / 20, "macro f1: ", f1macro/ 20, "micro f1: ", f1micro/ 20)

logreg()