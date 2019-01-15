#!/bin/bash

## 法人风险分析实验
## 需要配置python3环境
## 需要先确保python/data/legal/*数据存在。hive数据库中获取

cd python

echo 'Begin...'
python3 ./riskLegal.py

echo 'End. Outfile: python/data/risklegal.txt'

cd ..