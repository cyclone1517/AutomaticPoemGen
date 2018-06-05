#数据处理： 把标准的五言七言诗歌(zzcf.py正则后)数据进行分词和词频统计两步骤的操作
#输入文件： zzcf.txt   正则处理后的唐诗
#输出文件： wordflagfreq/a.txt  在data里还要创建一个文件夹统一存放不同词性的词频
#           wordflagfreq/m.txt
#           wordflagfreq/n.txt
#           wordflagfreq/v.txt

import time
import jieba.posseg as psg
import jieba.analyse

#jieba.enable_parallel(4)
#windows不支持并行jieba编程分词

content = open('../data/zzcf.txt').read()
#content = open('../data/poem.txt', encoding="utf-8").read()
#content = "寥落古行宫，宫花寂寞红"
#poem_words = [(x.word, x.flag) for x in psg.cut(content) if len(x.word) >= 2]
#print(poem_words)
rst_a = open('../data/wordflagfreq/a.txt', 'w+',encoding='utf-8')
rst_m = open('../data/wordflagfreq/m.txt', 'w+',encoding='utf-8')
rst_n = open('../data/wordflagfreq/n.txt', 'w+',encoding='utf-8')
rst_v = open('../data/wordflagfreq/v.txt', 'w+',encoding='utf-8')
rst_z = open('../data/wordflagfreq/z.txt', 'w+',encoding='utf-8')

cnt_a = 0
cnt_m = 0
cnt_n = 0
cnt_v = 0
cnt_z = 0
t1 = time.time()

print('ready adj')
for x in jieba.analyse.textrank(content,topK=500, allowPOS=('a')):
    rst_a.writelines(x+" ")
    cnt_a += 1
    if cnt_a%10==0:
        rst_a.write("\n")

print('ready m')
for x in jieba.analyse.textrank(content, topK=500, allowPOS=('m')):
    rst_m.writelines(x+" ")
    cnt_m += 1
    if cnt_m%10==0:
        rst_m.write("\n")

print('ready n')
for x in jieba.analyse.textrank(content, topK=500,allowPOS=('n')):
    rst_n.writelines(x+" ")
    cnt_n += 1
    if cnt_n%10==0:
        rst_n.write("\n")

print('ready verb')
for x in jieba.analyse.textrank(content,topK=500, allowPOS=('v')):
    rst_v.writelines(x+" ")
    cnt_v += 1
    if cnt_v%10==0:
        rst_v.write("\n")

print('ready zt')
for x in jieba.analyse.textrank(content,topK=500, allowPOS=('z')):
    rst_z.writelines(x+" ")
    cnt_z += 1
    if cnt_z%10==0:
        rst_z.write("\n")

print('all finished')
t2 = time.time()
tm_cost = t2-t1

print(tm_cost)
print("speed:  %s 词/秒" %(len(content)/tm_cost))
