#PoemGene头文件
import pinyin

#函数：得到高频拆分词序列
def getWords(preli):
    list = []
    for wordline in preli:
        wordsInLine = wordline.split(" ")
        wordsInLine.pop()       #弹出每行最后一个元素(换行符)
        list += wordsInLine
    return list

#函数：词性字数解析器
#每个词性最多连续两字
def wordDecoder(flagline):
    #print(flagline)
    length = len(flagline)
    char1 = flagline[0]
    char2 = None
    if length> 1:
        char2 = flagline[1]
    if char1 == char2:
        return char1, 2
    else:
        return char1, 1

#函数：判断词的平仄
def ispz(word, pz, num):
    temp = pinyin.get(word, format="numerical", delimiter=" ")
    templist = temp.split(" ")
    length = num
    cnt = 0
    while cnt < length:
        if pz[cnt] == 'p':
            if int((templist[cnt])[-1]) > 2:
                return False
        if pz[cnt] == 'z':
            if int((templist[cnt])[-1]) < 3:
                return False
        cnt = cnt +1
    return True

#函数：找到字的韵母
#注意输入字而不是词
def getyj(word):
    yj = pinyin.get(word, format="strip", delimiter=" ")
    yj = yj[1:]
    if yj[0] == 'h':
        yj = yj[1:]
    return yj

#函数：两个韵母是否相互押韵
#注意：截取字串区间前开后闭，range也是前开后闭
"""
def isyy(ym1,ym2):
    print("ym1="+ym1 + ",ym2="+ym2)
    for i in range (1,len(ym1)+1):                #长度遍历
        for j in range (0,len(ym1)-i-1):        #位置遍历
            if (ym1[j:j+i] in ym2):
                print(ym1[j:j+i] + ", " + ym2)
                return True
    return False
"""
def isyy(ym1,ym2):
    #print("ym1="+ym1, "ym2="+ym2)
    for i in range(1,len(ym1)+1):
        for j in range(0,len(ym1)-i+1):
            if ym1 in ym2 and ym1!='n' and ym1!='g' and ym1!='ng':
                return True
    for i in range(1,len(ym2)+1):
        for j in range(0,len(ym2)-i+1):
            if ym2 in ym1 and ym2!='n' and ym2!='g' and ym2!='ng':
                return True
    return False