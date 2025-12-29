N = int(input())
first = list(map(int, input().split()))
wait = []
need = 1
for x in first:
    while wait and wait[-1] == need:
        wait.pop()
        need += 1

    if x == need:
        need += 1
    else:
        wait.append(x)
while wait and wait[-1] == need:
    wait.pop()
    need += 1

print("Nice" if not wait else "Sad")