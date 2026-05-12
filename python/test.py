with open("二十大报告.txt","r") as f:
    txt=f.read()
import jieba
wo={}
print(txt)
words=jieba.cut(txt)
for word in words:
    if len(word)==1:
        continue
    wo[word]=wo.get(word,0)+1
print(wo)
