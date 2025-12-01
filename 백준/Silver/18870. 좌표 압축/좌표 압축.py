num = int(input())
num1 = list(map(int, input().split()))
uni_vals = sorted(set(num1))
rank = {}
for i in range(len(uni_vals)):
    # print(i)
    rank[uni_vals[i]] = i
    # print(rank)
# print(rank)
result = []
for x in num1:
    result.append(rank[x])

print(*result)