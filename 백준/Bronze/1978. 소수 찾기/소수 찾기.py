N= int(input())
num=list(map(int,input().split()))
cnt=0

for i in num:
    check=[]
    for j in range(1,i+1):
        if i%j==0:
            check.append(j)
    if check==[1,i]:
        cnt+=1
print(cnt)    
        