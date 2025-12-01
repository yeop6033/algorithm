a,b = map(int,input().split())
main=[]
for i in range(a):
    cat_main = str(input())
    main.append(cat_main)
sub=[]
for j in range(b):
    cat_sub = str(input())
    sub.append(cat_sub)
    
count=0
for x in sub:
    if x in main:
        count+=1
print(count)