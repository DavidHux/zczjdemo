

def countprodtype():
    print('Begin count product type...')
    typeset = {}
    tc = 0
    with open('data/lgpc/cnotptype.csv', 'w') as outfile:
        with open('data/lgpc/typeindex.csv', 'w') as outfileindex:
            with open('data/checkedP3.csv') as infile:
                next(infile)
                for line in infile:
                    sts = line.strip().split(',')
                    if(sts[3] == ''):
                        outfile.write(line)
                        continue
                    if sts[3] not in typeset:
                        typeset[sts[3]] = tc
                        tc += 1
                for key, value in typeset.items():
                    outfileindex.write(key+','+str(value)+'\n')
                print('End. total product type: ', len(typeset))


import numpy as np

def scale():
    print('Begin count salesvulome yeartotaloutput workers...')
    sale = []
    out = []
    worker = []
    with open('data/lgpc/fea.csv', 'w') as outfile:
        # with open('data/lgpc/sort.csv', 'w' ) as sortfile:
            with open('data/checkedP3.csv') as infile:
                next(infile)
                for line in infile:
                    sts = line.strip().split(',')
                    if(sts[5] != ''):
                        a = float(sts[5])
                        if a>=2 and a<=100000:
                            sale.append(a)
                    if(sts[9] != ''):
                        out.append(float(sts[9]))
                    if(sts[10] != ''):
                        worker.append(float(sts[10]))
                outfile.write('salesvulome: mean ' + str(np.mean(sale)) + ', median '+ str(np.median(sale))+'\n')
                outfile.write('yeartotaloutput: mean ' + str(np.mean(out)) + ', median '+ str(np.median(out))+'\n')
                outfile.write('workers: mean ' + str(np.mean(worker)) + ', median '+ str(np.median(worker))+'\n')
                # print(len(sale), len(out), len(worker))
                sale.sort()
                # print(sale)

import random
def separate():
    print("Seperate train and test data...")
    DATASIZE = 47455
    a = [i for i in range(DATASIZE)]
    random.shuffle(a)
    i = int(DATASIZE * 0.9)
    # train = a[:DATASIZE]
    test = a[i:]
    s = set(test)
    with open('data/lgpc/traindata.csv', 'w') as trainfile:
        with open('data/lgpc/testdata.csv', 'w') as testfile:
            with open('data/checkedP3.csv') as infile:
                count = 0
                next(infile)
                for line in infile:
                    if count in s:
                        testfile.write(line)
                    else:
                        trainfile.write(line)
                    count += 1
def feature01generate(infilename, outfilename):
    typedict = {}
    with open('data/lgpc/typeindex.csv') as infile:
        for line in infile:
            sts = line.strip().split(',')
            typedict[sts[0]] = int(sts[1])
    with open(outfilename, 'w') as outfile:
        with open(infilename) as infile:
            for line in infile:
                sts = line.strip().split(',')
                if sts[11] == '' or sts[11] == '-1':
                    continue
                sales = yeart = workers = 0.0
                if sts[5] == '':
                    sales = 600.0
                else:
                    sales = float(sts[5])
                    sales = 2 if sales < 2 else sales
                    sales = 100000 if sales > 100000 else sales
                if sts[9] == '':
                    yeart = 600.0
                else:
                    yeart = float(sts[9])
                    yeart = 2 if yeart < 2 else yeart
                    yeart = 100000 if yeart > 100000 else yeart
                if sts[10] == '':
                    workers = 35
                else:
                    workers = float(sts[10])
                    workers = 2 if workers < 2 else workers
                    workers = 5000 if workers > 5000 else workers

                scale = '2' if sts[7] == '' else sts[7]
                tyindex = typedict[sts[3]]

                outfile.write(scale + ' ' + str(sales) + ' ' + str(yeart) +' ' + str(workers))
                for i in range(1160):
                    if tyindex == i:
                        outfile.write(' 1')
                    else:
                        outfile.write(' 0')
                outfile.write(' ' + sts[11] + '\n')

def feature4ip():
    typedict = {}
    with open('data/lgpc/typeindex.csv') as infile:
        for line in infile:
            sts = line.strip().split(',')
            typedict[sts[0]] = int(sts[1])
    cou = 0
    with open('data/lgpc/val.txt', 'w') as outfile:
        with open('data/industryP.csv') as infile:
            next(infile)
            for line in infile:
                sts = line.strip().split(',')
                sales = yeart = workers = 0.0
                if sts[8] == '':
                    sales = 600.0
                else:
                    sales = float(sts[8])
                    sales = 2 if sales < 2 else sales
                    sales = 100000 if sales > 100000 else sales
                if sts[12] == '':
                    yeart = 600.0
                else:
                    yeart = float(sts[12])
                    yeart = 2 if yeart < 2 else yeart
                    yeart = 100000 if yeart > 100000 else yeart
                if sts[13] == '':
                    workers = 35
                else:
                    workers = float(sts[13])
                    workers = 2 if workers < 2 else workers
                    workers = 5000 if workers > 5000 else workers

                scale = '2' if sts[10] == '' else sts[10]
                if sts[3] not in typedict:
                    tyindex = -1 
                    cou += 1
                else:
                    tyindex = typedict[sts[3]]

                outfile.write(scale + ' ' + str(sales) + ' ' + str(yeart) +' ' + str(workers))
                for i in range(1160):
                    if tyindex == i:
                        outfile.write(' 1')
                    else:
                        outfile.write(' 0')
                outfile.write('\n')
    print(cou)

countprodtype()
scale()
separate()
feature01generate('data/lgpc/traindata.csv', 'data/lgpc/train.txt')
feature01generate('data/lgpc/testdata.csv', 'data/lgpc/test.txt')
feature4ip()