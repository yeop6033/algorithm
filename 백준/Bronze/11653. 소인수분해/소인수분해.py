import math

N = int(input())

while N > 1:
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            print(i)
            N = N // i
            break
    else:
        print(N)
        break
