from imblearn.under_sampling import RandomUnderSampler
import xgboost as xgb
import numpy as np

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

def xgboost():

    traindata = np.loadtxt('data/lgpc/train.txt')
    testdata = np.loadtxt('data/lgpc/test.txt')

    # truecount2 =  29579 # 32875
    # falsecount2 = 2814 # 3117
    FN = 1164

    X = traindata[:,:FN]
    Y = traindata[:,FN:].ravel()

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

    dtrain = xgb.DMatrix(X1, label=y_r)
    dtest = xgb.DMatrix(X_test, label=Y_test)

    param = {'max_depth': 6, 'eta': 0.3, 'silent': 1, 'objective': 'binary:logistic'}
    param['nthread'] = 4
    param['eval_metric'] = ['auc', 'error']

    evallist = [(dtest, 'eval'), (dtrain, 'train')]

    num_round = 100
    bst = xgb.train(param, dtrain, num_round, evallist)
    bst.save_model('temp/0001.model')
    # dump model
    bst.dump_model('temp/dump.raw.txt')

    preddata = np.loadtxt('data/lgpc/val.txt')
    pred_x = min_max_scaler.fit_transform(preddata)
    dpred = xgb.DMatrix(pred_x)

    ypred = bst.predict(dpred)
    print(ypred)

    xgb.plot_importance(bst)
    # dump model with feature map
    # bst.dump_model('temp/dump.raw.txt', 'temp/featmap.txt')
    # bst = xgb.Booster({'nthread': 4})  # init model
    # bst.load_model('model.bin')  # load data

xgboost()