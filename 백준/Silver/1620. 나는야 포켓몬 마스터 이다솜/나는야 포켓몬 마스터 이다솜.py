import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_to_name = {}
name_to_num = {}


for i in range(1, N+1):
    name = input().strip()
    num_to_name[str(i)] = name 
    name_to_num[name] = str(i)  
# print(num_to_name)

# # print(num_to_name[25])
result=()
for _ in range(M):
    quiz = input().strip()
    if quiz.isdigit():           
        print(num_to_name[quiz])
    else:                       
        print(name_to_num[quiz])
