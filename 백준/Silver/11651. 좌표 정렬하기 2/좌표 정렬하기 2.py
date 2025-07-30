N= int(input())
num_list=[]
for i in range(N):
    k=list(map(int,input().split()))
    num_list.append(k)

num_list.sort(key=lambda x:(x[1],x[0]))
for j in num_list:
    print(*j)