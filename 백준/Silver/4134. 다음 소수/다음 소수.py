import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    if n <= 2:
        print(2)
        continue

    # 짝수면 바로 다음 홀수부터 시작
    if n % 2 == 0:
        n += 1

    while True:
        x = n

        # 2보다 작은 건 소수 아님
        if x < 2:
            n += 1
            continue

        # 작은 소수들로 먼저 걸러주기 (속도 ↑)
        if x == 2 or x == 3 or x == 5:
            print(x)
            break
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
            n += 2
            continue

        # Miller–Rabin 시작
        d = x - 1
        s = 0
        # x-1 = d * 2^s 꼴로 분해
        while d % 2 == 0:
            d //= 2
            s += 1

        ok = True
        # 2, 7, 61 기저 → 2^32(대략 4.2e9) 이하에서 결정적이다
        for a in (2, 7, 61):
            if a >= x:
                continue

            # y = a^d mod x
            y = pow(a, d, x)

            if y == 1 or y == x - 1:
                continue  # 이 기저 a에서는 통과

            passed = False
            # 제곱하면서 x-1 나오는지 확인
            for _ in range(s - 1):
                y = (y * y) % x
                if y == x - 1:
                    passed = True
                    break

            if not passed:
                ok = False
                break

        if ok:
            print(x)
            break

        # 소수 아니면 다음 홀수
        n += 2
