#正则分词：对爬虫得到的数据做无关数据过滤
#输入文件npoem.txt
#输出文件zzcf.txt
import re

poemfile = open('../data/npoem.txt',encoding='UTF-8').read()

#key是用来测试的数据，可以不使用
key = r"白日依山尽，黄河入海流。一二三四五六七，七六五四三二一。一二三四五六。"
p1 = r"[\u4e00-\u9fa5]{5,7}[\u3002|\uff0c]"  #[汉字]{重复5-7次}[中文句号|中文逗号]
pattern1 = re.compile(p1)        #编译正则表达式
result = pattern1.findall(poemfile)   #搜索匹配的字符串，得到匹配列表

# r是什么意思？

with open('../data/zzcf.txt','w+') as f: #打开输出文件
    for x in result:
        f.write(x)    #遍历输出