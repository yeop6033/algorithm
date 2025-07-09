a, b, c = map(int, input().split())
sticks = sorted([a, b, c])

if sticks[0]+sticks[1]<=sticks[2]:
    print((sticks[0]+sticks[1])*2-1)
else:
    print(sum(sticks))