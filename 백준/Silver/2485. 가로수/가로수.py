import sys
input = sys.stdin.readline

N = int(input())
pos = []

for _ in range(N):
    pos.append(int(input()))


pos.sort()


diffs = []
for i in range(N-1):
    diffs.append(pos[i+1] - pos[i])



g = diffs[0] 


for d in diffs[1:]:
    a = g
    b = d
    while b != 0:
        a, b = b, a % b
    g = a  


answer = 0
for d in diffs:
    answer += (d // g) - 1

print(answer)
