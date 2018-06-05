#PoemGene2: 按词性解析模板
#PoemGene3: 加入平仄和七言，分出头文件
import random
import PoemHead

#函数：从高频拆分词中取组装词
def fetchWord(wordflag, num):
    word = ""
    if wordflag == 'n':
        word = nlist[random.randint(0, 299)]
    elif wordflag == 'v':
        word = vlist[random.randint(0, 299)]

    if num == 1:
        if random.randint(0,1) == 1:
            word = word[0:1]
        else:
            word = word[1:2]
    return word

#函数：根据不同的模板生成诗句
#输入参数：词性行nnvnn
def getPoemLine(flagline, modeline):
    length = len(modeline)
    cnt = 0
    poemline = ""
    while cnt<length:
        wordflag, num = PoemHead.wordDecoder(flagline)
        templine = fetchWord(wordflag, num)
        while not PoemHead.ispz(templine, modeline, num):
            templine = fetchWord(wordflag,num)
        poemline += templine
        flagline = flagline[num:]
        modeline = modeline[num:]
        cnt = cnt + num
    return poemline

#函数：打印一首诗
def poemPrint(mode,flagline):
    print(getPoemLine(flagline[0], mode[0]))
    print(getPoemLine(flagline[1], mode[1]))
    print(getPoemLine(flagline[2], mode[2]))
    print(getPoemLine(flagline[3], mode[3]))

#打开文件
adjs = open('../data/wordflagfreq/a.txt', encoding='utf-8').read()
nmbs = open('../data/wordflagfreq/m.txt', encoding='utf-8').read()
noues = open('../data/wordflagfreq/n.txt', encoding='utf-8').read()
verbs = open('../data/wordflagfreq/v.txt', encoding='utf-8').read()

#按行提取(为后面排除换行符元素)
ali = adjs.splitlines()
mli = nmbs.splitlines()
nli = noues.splitlines()
vli = verbs.splitlines()

#得到词集合
alist = PoemHead.getWords(ali)
mlist = PoemHead.getWords(mli)
nlist = PoemHead.getWords(nli)
vlist = PoemHead.getWords(vli)

#根据不同模板打印诗句
wordlist = []
mode51 = ['zzppz','ppzzp','pppzz','zzzpp']
mode52 = ['pppzz','zzzpp','zzppz','ppzzp']
mode71 = ['zzppzzp','ppzzzpp','ppzzppz','zzppzzp']
mode72 = ['zzpppzz','ppzzzpp','ppzzppz','zzppzzp']

#此为词性模板
flagline51 = ['nnvnn','nnvnn','nnvnn','nnnnv']
flagline71 = ['nnnnvvv','nnnnvvv','nnnnvvv','nnnnvvv']

switX = random.randint(0,3)
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

print(mode)
poemPrint(mode,flagline)