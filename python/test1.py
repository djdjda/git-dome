with open("city_GDP.csv","r",encoding="gbk") as f:
    f.readline()
    txt=f.readlines()
table=[]
dic={}
for line in txt:
    he=[]
    for i in line.split(",")[1:]:
      he.append(float(i))
    he.sort(reverse=True)
    dic.update({line.split(",")[0]:he[0]})
name=input("请输入所要查询的城市名：")
print("{:.2f}".format(dic[name]))   
