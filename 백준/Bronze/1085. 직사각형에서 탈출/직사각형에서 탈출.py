import math
x,y,w,h=map(int,input().split())
check=[]
# print(x,y,w
check.append(math.sqrt((x-w)**2+(y-h)**2))
check.append(abs(x-0))
check.append(abs(y-0))
check.append(abs(x-w))
check.append(abs(y-h))
print(min(check))