N= int(input())
num_list=[]
for i in range(N):
    k=list(map(int,input().split()))
    num_list.append(k)

num_list.sort()
for j in num_list:
    print(*j)