N,M=map(int,input().split())
card=list(map(int,input().split()))
max_card=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            total=card[i]+card[j]+card[k]
            if total<=M:
                max_card=max(max_card,total)
print(max_card)