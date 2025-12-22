import sys, re
input = sys.stdin.readline

while True:
    s = input()
    if not s:
        break

    line = s.rstrip('\n')   # 줄바꿈만 제거 (앞/뒤 공백은 유지)
    if line == '.':         # 종료 마커는 출력하지 않음
        break

    result = re.sub(r'[^()\[\]]', '', line)  # 괄호만 남기기

    stack = []
    ok = True

    for ch in result:
        if ch in '([':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                ok = False
                break
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                ok = False
                break
            stack.pop()

    print("yes" if ok and not stack else "no")
