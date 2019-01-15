def diffInIpAndCp():
    ipcount = cpcount = 0
    unionccount = 0
    ipdict = {}
    cpdict = {}
    udict = set()
    with open('data/ipnot48.csv', 'w') as outfile:
        with open('data/industry_product.csv') as infile:
            next(infile)
            for line in infile:
                sts = line.strip().split('","')
                if len(sts) != 48:
                    outfile.write(line)
                    continue
                ipcount += 1
                orgid = sts[1].replace('"', '')
                if orgid not in ipdict:
                    ipdict[orgid] = 0
                ipdict[orgid] += 1

    with open('data/cpnot104.csv', 'w') as outfile:    
        with open('data/test_report.csv') as infile:
            next(infile)
            for line in infile:
                sts = line.strip().split('","')
                if len(sts) != 104:
                    outfile.write(line)
                    continue
                cpcount += 1
                orgid = sts[1].replace('"', '')
                if orgid not in cpdict:
                    cpdict[orgid] = 0
                cpdict[orgid] += 1
                if orgid in ipdict:
                    unionccount += 1
                    udict.add(orgid)

    print("count industry products first, then count the nums of checked products which in ipc",
        "\nip size is ", ipcount,
        "\nipc num is ", len(ipdict),
        "\ncp size is ", cpcount, 
        "\ncpc num is ", len(cpdict),
        "\nunion p num is ", unionccount,
        "\nunion c size is ", len(udict))

def checkCompanyinIndustry():
    indset = set()
    with open('data/industry.csv') as infile:
        next(infile)
        for line in infile:
            sts = line.strip().split('","')
            if len(sts) != 110:
                continue
            indset.add(sts[0].replace('"', ''))
    with open('data/Industry_productIn.csv', 'w') as outfilein:
        with open('data/ipNotIn.csv', 'w') as outfile:
            with open('data/industry_product.csv') as infile:
                next(infile)
                for line in infile:
                    sts = line.strip().split('","')
                    if len(sts) != 48:
                        continue
                    if sts[1].replace('"', '') not in indset:
                        outfile.write(line)
                    else:
                        outfilein.write(line)

    with open('data/Checked_productIn.csv', 'w') as outfilein:
        with open('data/cpNotIn.csv', 'w') as outfile:
            with open('data/test_report.csv') as infile:
                next(infile)
                for line in infile:
                    sts = line.strip().split('","')
                    if len(sts) != 104:
                        continue
                    if sts[1].replace('"', '') not in indset:
                        outfile.write(line)
                    else:
                        outfilein.write(line)

def filterInductry():
    udict = set()
    with open('data/Industry_productIn.csv') as infile:
        for line in infile:
            sts = line.strip().split('","')
            if len(sts) != 48:
                print('err')
                continue
            orgid = sts[1].replace('"', '')
            udict.add(orgid)
    with open('data/Checked_productIn.csv') as infile:
        for line in infile:
            sts = line.strip().split('","')
            if len(sts) != 104:
                print('err 104')
                continue
            orgid = sts[1].replace('"', '')
            udict.add(orgid)

    with open('data/Industry_company.csv', 'w') as outfile:
        with open('data/industry.csv') as infile:
            next(infile)
            for line in infile:
                sts = line.strip().split('","')
                if len(sts) != 110:
                    continue
                if sts[0].replace('"', '') in udict:
                    outfile.write(line)

def filterFeature():
    inpa = [1, 4, 10, 11, 12, 16, 17, 22, 26, 27, 28, 33, 34]
    with open('data/industryP.csv', 'w') as outfile:
        with open('data/olddata/Industry_product1.csv') as infile:
            linec = 0
            for line in infile:
                sts = line.strip().split('","')
                if linec == 0:
                    outfile.write(sts[0].replace('"', ''))
                    for i in inpa:
                        outfile.write(","+sts[i])
                    outfile.write('\n')
                    linec += 1
                else:
                    outfile.write(sts[0].replace(' ', '').replace(',', '').replace('"', ''))
                    for i in inpa:
                        outfile.write(','+sts[i].replace(' ', '').replace(',', '').replace('"', ''))
                    outfile.write('\n')

    ckpa = [1, 50, 25, 26, 31, 23, 12, 13, 33, 32, 38]
    with open('data/checkedP.csv', 'w') as outfile:
        with open('data/olddata/Checked_product.csv') as infile:
            linec = 0
            for line in infile:
                sts = line.strip().split('","')
                if linec == 0:
                    outfile.write(sts[0].replace('"', ''))
                    for i in ckpa:
                        outfile.write(","+sts[i])
                    outfile.write('\n')
                    linec += 1
                else:
                    outfile.write(sts[0].replace(' ', '').replace(',', '').replace('"', ''))
                    for i in ckpa:
                        outfile.write(','+sts[i].replace(' ', '').replace(',', '').replace('"', ''))
                    outfile.write('\n')

def pnamedict():
    typeset = set()
    nameset = set()
    comset = set()
    with open('data/checkedP.csv') as infile:
        next(infile)
        for line in infile:
            sts = line.strip().split(',')
            typeset.add(sts[3])
            nameset.add(sts[6])
            comset.add(sts[1])
        print(len(typeset), len(nameset))
    
    incount1 = incount2 = incount3 = incount4 = 0
    notincount = notincount2 = 0
    with open('data/notprodname.csv', 'w') as outfile:
        with open('data/industryp.csv') as infile:
            next(infile)
            for line in infile:
                sts = line.strip().split(',')
                if sts[3] != '' and (sts[3] in typeset or sts[3] in nameset):
                    incount1 += 1
                elif sts[5] != '' and (sts[5] in typeset or sts[5] in nameset):
                    incount2 += 1
                elif sts[6] != '' and (sts[6] in typeset or sts[5] in nameset):
                    incount3 += 1
                elif sts[9] != '' and (sts[9] in typeset or sts[5] in nameset):
                    incount4 += 1
                else:
                    if sts[1] != '' and sts[1] in comset:
                        notincount += 1
                    else:
                        notincount2 += 1
                    outfile.write(line)
        
        print(incount1, incount2, incount3, incount4, notincount, notincount2)
def filterblankcheckedP():
    with open('data/checkedP3.csv', 'w') as outfile:
        with open('data/filteredCp.csv', 'w') as outfilef:
            with open('data/checkedP2.csv') as infile:
                for line in infile:
                    sts = line.strip().split(',')
                    if sts[3] == '':
                        outfilef.write(line)
                    else:
                        outfile.write(line)

def countprodtype():
    typeset = {}
    tc = 0
    with open('data/cnotptype.csv', 'w') as outfile:
        with open('data/typeindex.csv', 'w') as outfileindex:
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
                print(len(typeset))


import numpy as np

def scale():
    sale = []
    out = []
    worker = []
    with open('data/fea.csv', 'w') as outfile:
        # with open('data/sort.csv', 'w' ) as sortfile:
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
                print(len(sale), len(out), len(worker))
                sale.sort()
                print(sale)

import random
def separate():
    DATASIZE = 47455
    a = [i for i in range(DATASIZE)]
    random.shuffle(a)
    i = int(DATASIZE * 0.9)
    # train = a[:DATASIZE]
    test = a[i:]
    s = set(test)
    with open('data/traindata.csv', 'w') as trainfile:
        with open('data/testdata.csv', 'w') as testfile:
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
    with open('data/typeindex.csv') as infile:
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
                    if sales < 2 or sales > 100000:
                        sales = 600.0
                if sts[9] == '':
                    yeart = 600.0
                else:
                    yeart = float(sts[9])
                    if yeart < 2 or yeart > 100000:
                        yeart = 600.0
                if sts[10] == '':
                    workers = 35
                else:
                    workers = float(sts[10])
                    if workers < 2 or workers > 5000:
                        workers = 35

                scale = '2' if sts[7] == '' else sts[7]
                tyindex = typedict[sts[3]]

                outfile.write(scale + ' ' + str(sales) + ' ' + str(yeart) +' ' + str(workers))
                for i in range(1160):
                    if tyindex == i:
                        outfile.write(' 1')
                    else:
                        outfile.write(' 0')
                outfile.write(' ' + sts[11] + '\n')

def addrc():
    postdict = {}
    with open('data/industry.csv') as infile:
        next(infile)
        for line in infile:
            sts = line.strip().split('","')
            post = sts[33]
            if post not in postdict:
                postdict[post] = []
            postdict[post].append(line)
    for key,value in postdict.items():
        with open('data/addr/'+key+'.txt', 'w') as outfile:
            for l in value:
                outfile.write(l)

# def maxlenofaddr():
#     with open('data/addr/370102.txt') as infile:
#         for line in infile:
#             sts = line.split('","')

def countrisk(a):
    # p = 0.0
    neg = 0
    for i in a:
        if i == 0:
            neg += 1
    return float(neg) / len(a)
import math
def pearson(vector2):
    n = len(vector2)
    vector1 = [1] * n
    #simple sums
    sum1 = sum(float(vector1[i]) for i in range(n))
    sum2 = sum(float(vector2[i]) for i in range(n))
    #sum up the squares
    sum1_pow = sum([pow(v, 2.0) for v in vector1])
    sum2_pow = sum([pow(v, 2.0) for v in vector2])
    #sum up the products
    p_sum = sum([vector1[i]*vector2[i] for i in range(n)])
    #分子num，分母den
    num = p_sum - (sum1*sum2/n)
    den = math.sqrt((sum1_pow-pow(sum1, 2)/n)*(sum2_pow-pow(sum2, 2)/n))
    if den == 0:
        return 0.0
    return num/den


def legal():
    checkedCom = set()
    with open('data/fil_check.csv') as infile:
        # next(infile)
        for line in infile:
            sts = line.split(',')
            checkedCom.add(sts[1])
    print(len(checkedCom))
    legaldict = dict()
    com2legaldict = dict()

    with open('data/legal_company.csv') as infile:
        next(infile)
        for line in infile:
            sts = line.split('","')
            coid = sts[2].lstrip('0')
            # print(coid)
            if coid in checkedCom:
                com2legaldict[coid] = sts[1]
                legaldict[sts[1]] = []
    print(len(com2legaldict))
    with open('data/fil_check.csv') as infile:
        next(infile)
        for line in infile:
            sts = line.strip().split(',')
            if sts[1] in com2legaldict:
                a = 1 if sts[3] == '是' else 0
                legaldict[com2legaldict[sts[1]]].append(a)
            
    legaldict2 = dict()
    for key, value in legaldict.items():
        if len(value) >1:
            legaldict2[key] = countrisk(value)

    with open('data/risklegal.txt', 'w') as outfile:
        for key, value in sorted(legaldict2.items(), key=lambda item: (item[1],item[0]), reverse=True):
            # print(key, value)
            outfile.write(key +' '+  str(value)+ ' ' +str(len(legaldict[key])) + '\n')

def simaddrs():
    comdict = {}
    with open('data/simaddrs.txt') as infile:
        for line in infile:
            sts = line.strip().split(' ')
            # print(len(sts))
            comdict[sts[1]] = ''
            comdict[sts[4]] = ''
    
    with open('data/industry.csv') as infile:
        next(infile)
        for line in infile:
            sts = line.split('","')
            s = sts[0].replace('"', '')
            if s in comdict:
                comdict[s] = line
    
    ii = [0, 2, 3, 4, 5, 10, 12, 24, 32, 33, 41, 43]
    with open('data/simaddrs2.txt') as infile:
        with open('data/sim2.txt', 'w') as outfile:
            for line in infile:
                # print(line)
                sts = line.strip().split(' ')
                # print(sts)
                for i in [1, 4]:
                    # print(i)
                    line2 = comdict[sts[i]]
                    sts2 = line2.split('","')
                    for x in ii:
                        outfile.write(sts2[x].replace('"', '')+' ')
                    outfile.write('\n')
                outfile.write('\n')

# from efficient_apriori import apriori
# def ap():
#     transactions = [('eggs', 'bacon', 'eggs'),
#                     ('eggs', 'bacon', 'eggs'),
#                     ('soup', 'bacon', 'banana')]
#     itemsets, rules = apriori(transactions, min_support=0.5,  min_confidence=1)
    # print(rules)  # [{eggs} -> {bacon}, {soup} -> {bacon}]

def pattern():
    comtydict = {}
    with open('data/olddata/industry.csv') as infile:
        next(infile)
        for line in infile:
            sts = line.split('","')
            comtydict[sts[10]] = sts[11]
    with open('data/fil_legal2.csv') as infile:
        with open('data/pattern.txt', 'w') as outfile:
            prev = ''
            l = ''
            for line in infile:
                sts = line.split('","')
                
                if sts[1] != prev:
                    outfile.write(l+'\n')
                    prev = sts[1]
                    if sts[2] not in comtydict:
                        l = ''
                    else:
                        l = comtydict[sts[2]]
                else:
                    if sts[2] in comtydict:
                        l += ' ' + comtydict[sts[2]]
            outfile.write(l)
# def pa():
#     palist = []
#     with open('data/pattern.txt') as infile:
#         for line in infile:
#             sts = line.strip().split(' ')
#             if len(sts) <= 1:
#                 continue
#             palist.append(sts)
#     itemsets, rules = apriori(palist, min_support=0.11,  min_confidence=0.1)
#     print(rules)

def rate():
    typedict = {}
    totalgood = 0
    total = 0
    with open('data/olddata/Checked_product.csv') as infile:
        next(infile)
        for line in infile:
            sts = line.split('","')
            if sts[38] != '1' and sts[38] != '0':
                continue
            g = 0
            if sts[38] == '1':
                g = 1
            total += 1
            totalgood += g
            if sts[14] not in typedict:
                typedict[sts[14]] = [0, 0]
            typedict[sts[14]][0] += g
            typedict[sts[14]][1] += 1
    for key,value in typedict.items():
        print(key, value[0], value[1], float(value[0])/value[1])
    print(totalgood, total, float(totalgood)/total)

def simaddrs2():
    comdict = {}
    with open('data/simaddrs4.txt') as infile:
        for line in infile:
            sts = line.strip().split(' ')
            # print(len(sts))
            comdict[sts[1]] = ''
            comdict[sts[4].strip()] = ''
    
    with open('data/industry.csv') as infile:
        next(infile)
        for line in infile:
            sts = line.split('","')
            s = sts[0].replace('"', '')
            if s in comdict:
                comdict[s] = line
    
    addrdict = {}
    with open('data/simaddrs4.txt') as infile:
        for line in infile:
            sts = line.split(' ')
            if sts[0] not in addrdict:
                addrdict[sts[0]] = set()
            addrdict[sts[0]].add(sts[1])
            addrdict[sts[0]].add(sts[4].strip())

    ii = [0, 2, 3, 4, 5, 10, 12, 24, 32, 33, 41, 43, 94]
    with open('data/sim3.txt', 'w') as outfile:
        for _, value in addrdict.items():
            for x in value:
                if x not in comdict:
                    print("not in")
                    continue
                line2 = comdict[x]
                sts2 = line2.split('","')
                if len(sts2) < 44:
                    continue
                for x in ii:
                    outfile.write(sts2[x].replace('"', '')+', ')
                outfile.write('\n')
            outfile.write('\n')
        
def cccc():
    com2gddict = {}
    gddict = {}
    with open('data/fil_invest2.csv') as infile:
        for line in infile:
            sts = line.split('","')
            if sts[3] not in com2gddict:
                com2gddict[sts[3]] = []
            k = sts[0].replace('"', '') + ' ' + sts[1]
            com2gddict[sts[3]].append(k)
            gddict[k] = []
    count = 0
    with open('data/fil_check.csv') as infile:
        for line in infile:
            sts = line.strip().split(',')
            if sts[0] in com2gddict:
                b = 1 if sts[3] == '是' else 0
                count += 1
                for x in com2gddict[sts[0]]:
                    gddict[x].append(b)
    print(count)
    gdict2 = {}
    for key, value in gddict.items():
        if len(value) >= 1:
            gdict2[key] = countrisk(value)

    with open('data/riskinvest.txt', 'w') as outfile:
        for key, value in sorted(gdict2.items(), key=lambda item: (item[1],item[0]), reverse=True):
            # print(key, value)
            outfile.write(key +' '+  str(value)+ ' ' +str(len(gddict[key])) + '\n')


# diffInIpAndCp()
# checkCompanyinIndustry()
# filterInductry()
# filterFeature()
# pnamedict()
# filterblankcheckedP()
# countprodtype()
# scale()
# separate()
# feature01generate('data/traindata.csv', 'data/train.txt')
# feature01generate('data/testdata.csv', 'data/test.txt')
# addrc()
# legal()
# simaddrs2()
# print(pearson([1,1,1,1,1]))
# ap()
# pattern()
# pa()
# rate()
cccc()