import sys
N=int(input())
num_list=[]
for i in range(N):
    a = int(sys.stdin.readline())
    num_list.append(a)
num_list=sorted(num_list)
for i in num_list:
    print(i)