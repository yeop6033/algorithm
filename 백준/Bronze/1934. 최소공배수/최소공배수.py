T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    a, b = N, M  
    while b != 0:
        N, b = b, N % b

    gcd = N
    lcm = (a * M)//gcd
    print(lcm)
