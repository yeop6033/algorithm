T=int(input())
for i in range(T):
    num = int(input())
    for i in [25,10,5,1]:
        print(num//i,end=' ')
        num=num%i