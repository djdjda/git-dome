with open("competition.csv","r",encoding="gbk") as f:
  f.readline()
  txt=f.readlines()
total=0
count={}
for line in txt:
  table=line.split(",")
  
  count[table[1]]=count.get(table[1],0)+1
  total+=1
name=input("请输入所要查询的专业名：")
if name not in count:
  print("无此专业")
else:
  print("{:.1f}%".format(count[name]/total*100))

   