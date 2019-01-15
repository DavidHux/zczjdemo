def countrisk(a):
    # p = 0.0
    neg = 0
    for i in a:
        if i == 0:
            neg += 1
    return float(neg) / len(a)

def legal():
    checkedCom = set()
    with open('data/legal/fil_check.csv') as infile:
        # next(infile)
        for line in infile:
            sts = line.split(',')
            checkedCom.add(sts[1])
    print(len(checkedCom))
    legaldict = dict()
    com2legaldict = dict()

    with open('data/legal/legal_company.csv') as infile:
        next(infile)
        for line in infile:
            sts = line.split('","')
            coid = sts[2].lstrip('0')
            # print(coid)
            if coid in checkedCom:
                com2legaldict[coid] = sts[1]
                legaldict[sts[1]] = []
    print(len(com2legaldict))
    with open('data/legal/fil_check.csv') as infile:
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

legal()