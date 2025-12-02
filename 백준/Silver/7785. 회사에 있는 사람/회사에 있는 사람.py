import sys
input = sys.stdin.readline

num = int(input())
com_in = set()

for _ in range(num):
    name, check = input().split()
    if check == 'enter':
        com_in.add(name)
    else:  # 'leave'
        com_in.discard(name)   # remove 써도 되는데 discard가 에러 안 나서 더 안전

for name in sorted(com_in, reverse=True):
    print(name)
