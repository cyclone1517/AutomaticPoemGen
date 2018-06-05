#打开文件
adjs = open('../data/wordflagfreq/a.txt',encoding='utf-8').read()
nmbs = open('../data/wordflagfreq/m.txt',encoding='utf-8').read()
noues = open('../data/wordflagfreq/n.txt',encoding='utf-8').read()
verbs = open('../data/wordflagfreq/v.txt',encoding='utf-8').read()

#按行提取(排除换行符元素干扰)
ali = adjs.splitlines()
mli = nmbs.splitlines()
nli = noues.splitlines()
vli = verbs.splitlines()

#初始化词集合
alist = []
mlist = []
nlist = []
vlist = []

#得到词集合
for i in ali:
    alist.append(ali.split(' '))
for i in mli:
    mlist.append(mli.split(' '))
for i in nli:
    nlist.append(nli.split(' '))
for i in vli:
    vlist.append(vli.split(' '))


for i in alist:
    print(i)