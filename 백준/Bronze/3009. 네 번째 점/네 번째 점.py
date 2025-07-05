a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
check=a+b+c
x=[check[0],check[2],check[4]]
y=[check[1],check[3],check[5]]

for i in x:
    if x.count(i)==1:
        x4=i
for i in y:
    if y.count(i)==1:
        y4=i

print(x4,y4)