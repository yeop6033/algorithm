a,b = map(int,input().split())
# print(a,b)
num ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=''

while a:
    s += str(num[a%b])
    a //= b

print(s[::-1])
