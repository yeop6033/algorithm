import sys
import math

M, N = map(int, sys.stdin.readline().split())

# 소수 체크 리스트
prime = [True] * (N + 1)
prime[0] = prime[1] = False  # 0,1는 소수 아님

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(N)) + 1):
    if prime[i]:
        for j in range(i * i, N + 1, i):
            prime[j] = False

# 출력
for i in range(M, N + 1):
    if prime[i]:
        print(i)
