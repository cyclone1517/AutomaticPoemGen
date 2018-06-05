#PoemGene2: 按词性解析模板
#PoemGene3: 加入平仄和七言，分出头文件
#PoemGene3: 加入韵脚
#问题：没有er ong的形容词韵脚，打算手动补齐
import random
import PoemHead

#函数：从高频拆分词中取组装词
def fetchWord(wordflag, num):
    word = ""
    if wordflag == 'n':
        word = nlist[random.randint(0, nlen-1)]
    elif wordflag == 'v':
        word = vlist[random.randint(0, vlen-1)]
    elif wordflag == 'a':
        word = alist[random.randint(0, alen-1)]
    elif wordflag == 'm':
        word = mlist[random.randint(0, mlen-1)]
    elif wordflag == 'z':
        word = zlist[random.randint(0, zlen-1)]

    if len(word)>2:
        word = word[0:2]
    if num == 1:
        if random.randint(0,1) == 1:
            word = word[0:1]
        else:
            word = word[1:2]
    return word

#函数：根据不同的模板生成诗句
#输入参数：词性行nnvnn
def getPoemLine(flagline, modeline, yj):
    length = len(modeline)
    cnt = 0
    poemline = ""
    while cnt<length:
        wordflag, num = PoemHead.wordDecoder(flagline)
        templine = fetchWord(wordflag, num)
        if yj == None:
            while not PoemHead.ispz(templine, modeline, num):
                templine = fetchWord(wordflag,num)
        else:
            while (not PoemHead.ispz(templine, modeline, num)) or (not PoemHead.isyy(yj,PoemHead.getyj(templine[-1]))):
                #print(PoemHead.isyy(yj,PoemHead.getyj((wordlist[-1])[-1])))
                templine = fetchWord(wordflag, num)
        poemline += templine
        wordlist.append(templine)
        flagline = flagline[num:]
        modeline = modeline[num:]
        cnt = cnt + num
    return poemline

#函数：打印一首诗
def poemPrint(mode,flagline):
    print(getPoemLine(flagline[0], mode[0], None))
    print(getPoemLine(flagline[1], mode[1], None))
    yj = PoemHead.getyj((wordlist[-1])[-1])
    print(getPoemLine(flagline[2], mode[2], None))
    print(getPoemLine(flagline[3], mode[3], yj))

#打开文件
adjs = open('../data/wordflagfreq/a.txt', encoding='utf-8').read()
nmbs = open('../data/wordflagfreq/m.txt', encoding='utf-8').read()
noues = open('../data/wordflagfreq/n.txt', encoding='utf-8').read()
verbs = open('../data/wordflagfreq/v.txt', encoding='utf-8').read()
zts = open('../data/wordflagfreq/z.txt', encoding='utf-8').read()

#按行提取(为后面排除换行符元素)
ali = adjs.splitlines()
mli = nmbs.splitlines()
nli = noues.splitlines()
vli = verbs.splitlines()
zli = zts.splitlines()

#得到词集合
alist = PoemHead.getWords(ali)
mlist = PoemHead.getWords(mli)
nlist = PoemHead.getWords(nli)
vlist = PoemHead.getWords(vli)
zlist = PoemHead.getWords(zli)
alen = len(alist)
mlen = len(mlist)
nlen = len(nlist)
vlen = len(vlist)
zlen = len(zlist)

#根据不同模板打印诗句
mode51 = ['zzppz','ppzzp','pppzz','zzzpp']
mode52 = ['pppzz','zzzpp','zzppz','ppzzp']
mode71 = ['zzppzzp','ppzzzpp','ppzzppz','zzppzzp']
mode72 = ['zzpppzz','ppzzzpp','ppzzppz','zzppzzp']

#此为词性模板
flagline51 = ['nnvnn','nnvnn','nnvnn','nnnna']
flagline71 = ['nnnnvvv','nnzznzz','nnnnvvv','nnnnvva']

switX = random.randint(0, 3)
mode = mode51
flagline = flagline51
if switX == 1:
    mode = mode52
    flagline = flagline51
elif switX == 2:
    mode = mode71
    flagline = flagline71
elif switX == 3:
    mode = mode72
    flagline = flagline71

wordlist = []
poemPrint(mode, flagline)