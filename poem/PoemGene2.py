#PoemGene2: 按词性解析模板
import random

#函数：得到高频拆分词序列
def getWords(preli):
    list = []
    for wordline in preli:
        wordsInLine = wordline.split(" ")
        wordsInLine.pop()       #弹出每行最后一个元素(换行符)
        list += wordsInLine
    return list

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

#函数：词性字数解析器
#每个词性最多连续两字
def wordDecoder(mode):
    length = len(mode)
    char1 = mode[0]
    char2 = None
    if length> 1:
        char2 = mode[1]
    if char1 == char2:
        return char1, 2
    else:
        return char1, 1

#函数：根据不同的模板生成诗句
def getPoemLine(mode):
    length = len(mode)
    cnt = 0
    poemline = ""
    while cnt<length:
        wordflag, num = wordDecoder(mode)
        poemline += fetchWord(wordflag,num)
        mode = mode[num:]
        cnt = cnt + num

    return poemline

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
alist = getWords(ali)
mlist = getWords(mli)
nlist = getWords(nli)
vlist = getWords(vli)

#根据不同模板打印诗句
wordlist = []
print(getPoemLine("nnvnn"))
print(getPoemLine("nnvnn"))
print(getPoemLine("nnvnn"))
print(getPoemLine("nnnnv"))
