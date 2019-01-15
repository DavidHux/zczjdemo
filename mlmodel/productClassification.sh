#!/bin/bash

## 产品分类实验，使用logisticRegression等分类器对产品特征向量进行分类
## 需要配置python3环境
## 需要先确保python/data/lgpc/checkedP3.csv数据存在。执行com.njuics.preprocess.Select1.java从hive数据库中获取

cd python
echo 'Begin preprocessing...'
python3 ./productClassificationPreprocess.py
echo "Begin traning..."
python3 ./logisticRegressionPC.py
cd ..