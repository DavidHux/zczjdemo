import xgboost as xgb
import numpy as np
from sklearn import preprocessing


def xgboostpred():
    # traindata = np.loadtxt('data/lgpc/train.txt')
    min_max_scaler = preprocessing.MinMaxScaler()
    # X1 = min_max_scaler.fit_transform(X_r)

    # bst.load_model('temp/0001.model')  # load data
    bst = xgb.Booster({'nthread': 4})  # init model
    bst.load_model('temp/0001.model')
    preddata = np.loadtxt('data/lgpc/val.txt')
    pred_x = min_max_scaler.fit_transform(preddata)
    dpred = xgb.DMatrix(pred_x)

    ypred = bst.predict(dpred)
    with open('temp/pred.txt', 'w') as outfile:
        for i in ypred:
            outfile.write(str(i)+'\n')
    aaadict = {}
    with open('data/industryP.csv') as infile:
        next(infile)
        counttt = 0
        for line in infile:
            sts = line.split(',')
            aaadict[sts[0]] = ypred[counttt]
            counttt += 1
    
    with open('data/ippred.txt', 'w') as outfile:
        for key, value in sorted(aaadict.items(), key=lambda item: (item[1],item[0]), reverse=True):
            # print(key, value)
            outfile.write(key +' '+  str(value) + '\n')
    # print(ypred)

xgboostpred()