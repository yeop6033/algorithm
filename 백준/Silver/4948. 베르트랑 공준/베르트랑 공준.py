import sys

MAX = 123456 * 2  # 246912까지 필요

# 1) 0 ~ MAX까지 소수 여부를 미리 구해두기 (에라토스테네스의 체)
is_prime = [True] * (MAX + 1)
is_prime[0] = False
is_prime[1] = False

# 소수 판별 전처리
for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:  # i가 소수라면
        # i의 배수들은 전부 소수가 아님
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

# 2) 입력을 받으면서 (n, 2n] 구간에서 소수 개수 세기
while True:
    line = sys.stdin.readline()
    if not line:
        break
    test_case = int(line)

    if test_case == 0:
        break

    count = 0

    # (test_case, 2*test_case] 구간에서 소수 개수 세기
    for num in range(test_case + 1, 2 * test_case + 1):
        if is_prime[num]:
            count += 1

    print(count)
