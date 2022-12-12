n = int(input())
b1, b2 = map(int, input().split())
result = 0

for _ in range(n):
    a, b, c, d = map(int, input().split())
    if a <= b1 <= c and b <= b2 <= d:
        result += 1
print("Yes" if result > 0 else "No")