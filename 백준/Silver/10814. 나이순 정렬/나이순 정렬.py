N=int(input())
list_age=[]
for i in range(N):
    a=list(input().split())
    list_age.append(a)
list_age.sort(key=lambda x :int(x[0]))

for j in list_age:
    print(' '.join(map(str,j)))