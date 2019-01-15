#!/bin/bash

## 地址相似度检测实验
## 需要配置python3和c++环境
## 需要先确保python/data/lgpc/industry.csv数据存在。hive数据库中获取

cd python

echo 'Begin preprocessing...'
python3 ./addressSimilarity.py

echo "Begin traning..."
if [ ! -e temp/bktree ]; then
    g++-8 bk-tree.cpp -o temp/bktree -std=c++17 -lstdc++fs
fi
./temp/bktree

echo 'End. Outfile: python/data/simaddrs.txt'

cd ..