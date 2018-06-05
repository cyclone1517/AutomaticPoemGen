import random
import time
import firstpinyin

word_file = '../data/freqword.txt'
pinyin_file = '../data/frewordPinyin.txt'
dataset = open(word_file,encoding='utf-8').readlines()
outfile = open(pinyin_file,"w+",encoding='utf-8')
list = []
for word in dataset:
    outfile.write(firstpinyin.get(word, format="strip") + " ")
    i = 0
    while i<len(word):
        if word[i:i+2]!="\n":
            list.append(word[i:i+2])
        i=i+3

# sentence = ""
count = 0
num = 0

while num < 4:
    i = random.randint(1, len(list)-1)
    print(list[i], end="")
    time.sleep(0.5)
    count += 1
    if count == 2:
        print("\n")
        num += 1
        count = 0

# print(sentence)


