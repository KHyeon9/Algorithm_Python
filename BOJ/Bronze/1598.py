a, b = map(int, input().split())

a = a - 1
b = b - 1

n1 = a % 4
n2 = b % 4
n3 = a // 4
n4 = b // 4

r1 = abs(n1 - n2)
r2 = abs(n3 - n4)

print(r1 + r2)