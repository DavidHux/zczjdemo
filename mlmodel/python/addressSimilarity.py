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

addrc()