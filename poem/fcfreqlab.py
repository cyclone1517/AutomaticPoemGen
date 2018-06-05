import jieba
import  nltk

strs='1、大专以上学历，年龄在18-28岁之间；2、计算机相关专业、自动化、测控、生仪、机电、数学、物理等等理工科专业优先；' \
     '3、热爱软件开发事业、有较强的逻辑思维能力，对IT行业抱有浓厚的兴趣并有志于在IT行业长远发展，创造个人价值（非销售、非保险岗位）；4、有无相关经验均可，欢迎优秀的应届大学毕业生' \
     '5、渴望能有一项扎实的技术、获得一份有长远发展、稳定、有晋升空间的工作；、学习能力强，工作热情高，富有责任感，工作认真、细致、敬业，责任心强；'
text1=jieba.cut(strs)
fd=nltk.FreqDist(text1)
keys=fd.keys()
item=fd.items()
print(' '.join(keys))
dicts=dict(item)
sort_dict=sorted(dicts.items(),key=lambda d:d[1],reverse=True)
print(sort_dict)