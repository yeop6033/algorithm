n = int(input())
num1_list = list(map(int, input().split()))
m = int(input())
num2_list = list(map(int, input().split()))

s = set(num1_list)  # 여기서 한 번만 set으로

result = []
for x in num2_list:
    if x in s:
        result.append(1)
    else:
        result.append(0)

print(*result)
