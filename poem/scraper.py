#爬虫示例：爬下来数据有限，想得到更多数据请具体操作修改url实现

import urllib3
from bs4 import BeautifulSoup

file = open('../data/poem.txt', "wb+")
'''
#被反爬时使用
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=Certifi.where()
)
'''
http = urllib3.PoolManager()
url = 'http://so.gushiwen.org'
r = http.request('GET', url+'/gushi/tangshi.aspx')  #请求网页
#url = 'http://www16.zzu.edu.cn/qtss/zzjpoem1.dll/query';
#r = http.request('GET',url)

soup=BeautifulSoup(r.data, 'html.parser')  #BeautifulSoup 的构造方法,得到一个文档的对象
main = soup.find('div', class_="main3")    #可以打开网页，点右键检查看一下main3/left在网页中是什么
content = main.find('div', class_="left")

for link in content.find_all('a'):
    next = http.request('GET', url+link.get('href'))
    soup1 = BeautifulSoup(next.data, 'html.parser')
    poem = soup1.find('div', class_="contson")
    file.write(poem.get_text().encode('utf-8'))

