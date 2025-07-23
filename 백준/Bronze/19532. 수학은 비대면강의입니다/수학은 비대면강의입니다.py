a, b, c, d, e, f = map(int, input().split())

num = a * e - b * d
x = (c * e - b * f) // num
y = (a * f - c * d) // num

print(x, y)
