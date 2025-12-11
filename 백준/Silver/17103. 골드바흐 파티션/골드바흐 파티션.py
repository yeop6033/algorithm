import sys
input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]

max_n = max(nums)  # 필요한 최대 N까지만 소수 구하면 됨
# print(max_n)
# 1. 에라토스테네스의 체로 소수 테이블 만들기
is_prime = [True] * (max_n + 1)
is_prime[0] = is_prime[1] = False
# print(is_prime)

for i in range(2, int(max_n ** 0.5) + 1):
    if is_prime[i]:
        # i*i보다 작은 배수는 이미 이전 소수들에서 지워졌으므로 i*i부터 시작
        for j in range(i * i, max_n + 1, i):
            is_prime[j] = False

# 2. 소수 리스트 만들기
primes = [i for i in range(2, max_n + 1) if is_prime[i]]

# 3. 각 N에 대해 골드바흐 파티션 개수 세기
for N in nums:
    cnt = 0
    for p in primes:
        if p > N // 2:  # p <= N-p 조건 만족하는 범위까지만
            break
        if is_prime[N - p]:
            cnt += 1
    print(cnt)
