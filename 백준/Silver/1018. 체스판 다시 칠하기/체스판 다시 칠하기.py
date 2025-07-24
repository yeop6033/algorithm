N,M=map(int,input().split())
list_T=[]
min_paint=64
for i in range(N):
    line=list(map(str,input()))
    list_T.append(line)

for j in range(N-7):
    for k in range(M-7):
        paintw=0
        paintb=0
        for x in range(8):
            for y in range(8):
                check = list_T[j+x][k+y]
                if (x+y)%2==0:
                    if check !='W':
                        paintw+=1
                    if check !='B':
                        paintb+=1
                else:
                    if check!='B':
                        paintw+=1
                    if check!='W':
                        paintb+=1
        min_paint=min(min_paint,paintb,paintw)
print(min_paint)



