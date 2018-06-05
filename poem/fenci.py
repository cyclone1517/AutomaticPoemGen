#分词：得到分词结果
#输入文件zzcf.txt
#输出文件fenci.txt

#coding:utf-8
import jieba.posseg as psg

#poemfile = codecs.open('../data/poem.txt',encoding='UTF-8')
poemfile = open('../data/poem.txt', encoding='UTF-8').read()

poem_words = [(x.word, x.flag) for x in psg.cut(poemfile) if len(x.word) >= 2]
print('fenci finished...')
# x.word是词, x.flag是词性
print(len(poem_words))

# w+
# 1. 文件存在，则清空(也即写入空);
# 2. 文件不存在，则创建文件 ;
# 3. 文件流定位到开始位置， 所以read() 会得到空。

fa = open('../data/wordflag/a.txt', 'w+')
fm = open('../data/wordflag/m.txt', 'w+')
fn = open('../data/wordflag/n.txt', 'w+')
fv = open('../data/wordflag/v.txt', 'w+')

for x in poem_words:
    if 'a' in x:
        fa.write('{0}\t{1}\n'.format(x[0], x[1]))
    if 'm' in x:
        fm.write('{0}\t{1}\n'.format(x[0], x[1]))
    if 'n' in x:
        fn.write('{0}\t{1}\n'.format(x[0], x[1]))
    if 'v' in x:
        fv.write('{0}\t{1}\n'.format(x[0], x[1]))
