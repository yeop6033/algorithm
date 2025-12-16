import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    count=0
    ch = input().strip()
    ok = True
    # count = len(ch)
    for i in ch:
        if i =='(':
            count +=1
        else:
            if count == 0 :
                ok = False
                break
            count -=1
    if ok and count ==0:
        print('YES')
    else:
        print('NO')  