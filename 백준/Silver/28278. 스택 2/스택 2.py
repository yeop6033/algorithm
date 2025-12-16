import sys
input = sys.stdin.readline
    
stack = []
N = int(input())

for _ in range(N):
    cmd = input().split()   # 항상 리스트로 받기

    test_num = int(cmd[0])

    if test_num == 1:          # 예: 1 x
        check_num = int(cmd[1])
        stack.append(check_num)

    elif test_num == 2:        # 값 없음
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif test_num == 3:
        print(len(stack))

    elif test_num == 4:
        print(1 if not stack else 0)

    elif test_num == 5:
        print(stack[-1] if stack else -1)
