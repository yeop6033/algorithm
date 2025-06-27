a,b,v = map(int,input().split())
# print(v,a,b)

cnt=1
locat=0

if (v-b)%(a-b)==0:
    day = (v-b)//(a-b)
    print(day)
else:
    day = (v-b)//(a-b)+1
    print(day)
