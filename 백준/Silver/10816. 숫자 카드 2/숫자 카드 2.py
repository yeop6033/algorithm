n = int(input())
nums1 = list(map(int, input().split()))

m = int(input())
nums2 = list(map(int, input().split()))

dic = {}
for x in nums1:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

for x in nums2:
    if x in dic:
        print(dic[x], end=' ')
    else:
        print(0, end=' ')
