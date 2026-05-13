def func(a):
  return (a+1)**a-a**(a-1)
while 1:
  a=int(input("输入2~8的偶数，0退出："))
  if a==0:
    break
  elif a%2:
    print("输入错误")
  elif a<2 or a>8:
    print("输入错误")
  else:
    print(func(a))
    