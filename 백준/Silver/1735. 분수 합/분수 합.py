i,N=map(int,input().split())
j,M=map(int,input().split())
a,b=N,M
while b!=0:
    N,b=b, N%b
gcd=N
lcm=(a*M)//gcd
i = i*(lcm//a)
j = j*(lcm//M)
num=i+j
# print(i,j,N,M)
# print(lcm,num)
c,d =lcm,num
while d !=0:
    lcm,d=d,lcm%d
gcd1=lcm
# print(gcd1)
print(num//lcm, c//lcm)
    