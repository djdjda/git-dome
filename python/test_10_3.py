def check(n):
  for i in range(2,n//2+1):
    if n%i==0:
      return 0
  return 1
total=0
for i in range(51,101):
  if check(i):
    total+=1
    print(i,end=" ")
print("素数总数为：{}".format(total))