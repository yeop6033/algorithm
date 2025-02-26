num_check = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N,B = input().split(" ")
N = ''.join(reversed(N))
B = int(B)
total = 0
for x in range(len(N)-1,-1,-1):
    sum = num_check.index(N[x])* (B**x)
    total +=sum

print(total)