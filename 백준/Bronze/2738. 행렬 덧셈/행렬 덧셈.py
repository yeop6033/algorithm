# 입력 받기
n, m = map(int, input().split())

# 행렬 A 입력 받기
matrix_a = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix_a.append(row)

# 행렬 B 입력 받기
matrix_b = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix_b.append(row)

# 두 행렬을 더하기
result = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))
