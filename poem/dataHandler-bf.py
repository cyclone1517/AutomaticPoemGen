#数据处理： 把标准的五言七言诗歌数据进行分词和词频统计两步骤的操作
#输入文件： poem.txt
#输出文件： wordflagfreq/a.txt
#           wordflagfreq/m.txt
#           wordflagfreq/n.txt
#           wordflagfreq/v.txt

import time
import jieba.analyse

#jieba.enable_parallel(4)
#windows不支持并行jieba编程分词

content = open('../data/poem.txt', encoding="utf-8").read()
rst_a = open('../data/wordflagfreq/a.txt', 'w+',encoding='utf-8')
rst_m = open('../data/wordflagfreq/m.txt', 'w+',encoding='utf-8')
rst_n = open('../data/wordflagfreq/n.txt', 'w+',encoding='utf-8')
rst_v = open('../data/wordflagfreq/v.txt', 'w+',encoding='utf-8')

cnt_a = 0
cnt_m = 0
cnt_n = 0
cnt_v = 0
t1 = time.time()

for x in jieba.analyse.textrank(content, topK=300, allowPOS=('a','m','n','v')):
    if 'a' in x:
        rst_a.writelines(x+" ")
        cnt_a += 1
        if cnt_a%10==0:
            rst_a.write("\n")
    if 'm' in x:
        rst_m.writelines(x+" ")
        cnt_m += 1
        if cnt_m%10==0:
            rst_m.write("\n")
    if 'n' in x:
        rst_n.writelines(x+" ")
        cnt_n += 1
        if cnt_n %10==0:
            rst_n.write("\n")
    if 'v' in x:
        rst_v.writelines(x+" ")
        cnt_v += 1
        if cnt_v%10==0:
            rst_v.write("\n")
t2 = time.time()
tm_cost = t2-t1

print(tm_cost)
print("speed:  %s 词/秒" %(len(content)/tm_cost))
