import math
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
list_num=[]
list_num.append(a)
list_num.append(b)
list_num.append(c)
list_num.append(d)
list_num.append(e)
list_num=sorted(list_num)
print(sum(list_num)//len(list_num))
print(list_num[2])

