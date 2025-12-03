num_A,num_B = map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
a_b_ma=len(a-b)
b_a_ma=len(b-a)
result=a_b_ma+b_a_ma
print(result)