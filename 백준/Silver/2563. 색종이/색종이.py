area = [[0] * 100 for _ in range(100)]
paper_num=int(input())
for i in range(paper_num):
    x,y=map(int,input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            area[j][k] = 1
sum_area = sum(sum(row) for row in area)
print(sum_area)