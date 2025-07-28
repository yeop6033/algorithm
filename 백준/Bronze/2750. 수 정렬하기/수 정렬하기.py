N=int(input())
list_num=[]
for i in range(N):
    num=int(input())
    list_num.append(num)
    list_num=sorted(list_num)
for j in list_num:
    print(j)
