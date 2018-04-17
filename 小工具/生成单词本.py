#将网上下载的单词本格式化处理并生成要求格式的txt文件
#已测试通过
from re import compile,match

temps = []
regex = compile("^\w+")

file1 = open("2016英语六级高频核心词汇表.txt","r")
file2 = open("格式化单词表.txt","w")

lines = file1.readlines()
file1.close()
print("数据共计",len(lines)-1,"行")
for line in lines:
    word = match(regex, line)
    if word is not None:
        temps.append(word.group(0))

for temp in temps:
    file2.write(temp + "\n")
file2.close()


