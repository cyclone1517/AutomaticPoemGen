#分词：得到分词结果
#备份：处理poem
#输入文件zzcf.txt
#输出文件fenci.txt

#coding:utf-8
import jieba.posseg as psg

#poemfile = codecs.open('../data/poem.txt',encoding='UTF-8')
poemfile = open('../data/poem.txt',encoding='UTF-8').read()

poem_words = [(x.word, x.flag) for x in psg.cut(poemfile) if len(x.word) >=1]
# x.word是词, x.flag是词性
print(len(poem_words))

# w+
# 1. 文件存在，则清空(也即写入空);
# 2. 文件不存在，则创建文件 ;
# 3. 文件流定位到开始位置， 所以read() 会得到空。

with open('../data/fenci.txt','w+') as f:
    for x in poem_words:
        f.write('{0}\t{1}\n'.format(x[0],x[1]))
