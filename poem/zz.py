import re
'''
key = r"<h1>hello world<h1>"#源文本
p1 = r"<h1>.+<h1>"#我们写的正则表达式，下面会将为什么
pattern1 = re.compile(p1)
print(pattern1.findall(key))#发没发现，我怎么写成findall了？咋变了呢？
'''

key = r"白日依山尽，黄河入海流。一二三四五六七，七六五四三二一。一二三四五六。"
p1 = r"[\u4e00-\u9fa5]{5,7}[\u3002|\uff0c]"
pattern1 = re.compile(p1)
print(pattern1.findall(key))

# r是什么意思？