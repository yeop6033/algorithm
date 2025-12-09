import sys

input = sys.stdin.readline

test_num = list(map(int, input().split()))

primes = []

for i in range(test_num[0],test_num[1]+1):   
    x = i

    
    if x < 2:
        continue

    # 작은 소수 빠른 처리
    if x == 2 or x == 3 or x == 5:
        primes.append(x)
        continue

    # 2,3,5의 배수는 소수 아님
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        continue

    # -------- 여기서부터 Miller–Rabin --------
    d = x - 1
    s = 0
    
    while d % 2 == 0:
        d //= 2
        s += 1

    ok = True 

    
    for a in (2, 7, 61):
        if a >= x:
            continue

        
        y = pow(a, d, x)

        
        if y == 1 or y == x - 1:
            continue

        passed = False
       
        for _ in range(s - 1):
            y = (y * y) % x
            if y == x - 1:
                passed = True
                break

        
        if not passed:
            ok = False
            break


    if ok:
        primes.append(x)


for p in primes:
    print(p)


