import random

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

#函数：得到高频拆分词
def getWords(preli):
    list = []
    for wordline in preli:
        wordsInLine = wordline.split(" ")
        wordsInLine.pop()       #弹出每行最后一个元素(换行符)
        list += wordsInLine
    return list

#得到词集合
alist = getWords(ali)
mlist = getWords(mli)
nlist = getWords(nli)
vlist = getWords(vli)

wordsInPoem = []
#函数：根据不同的模板生成诗句
def getPoemLine(mode):
    strline = ""
    if mode=="212":
        strline += nlist[random.randint(0, 299)]
        if random.randint(0,1) == 1:
            strline += vlist[random.randint(0, 299)][0:1]
        else:
            strline += vlist[random.randint(0, 299)][1:2]
        strline += nlist[random.randint(0, 299)]
    if mode=="221":
        strline += nlist[random.randint(0, 299)]
        strline += nlist[random.randint(0, 299)]
        if random.randint(0,1) == 1:
            strline += alist[random.randint(0, 299)][0:1]
        else:
            strline += alist[random.randint(0, 299)][1:2]
    return strline

#根据不同模板打印诗句
print(getPoemLine("212"))
print(getPoemLine("212"))
print(getPoemLine("212"))
print(getPoemLine("221"))
