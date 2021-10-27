a = [int(input())for _ in range(5)]

r1 = a[0] + (max(a[4] - 30, 0) * a[1]) * 21
r2 = a[2] + (max(a[4] - 45, 0) * a[3]) * 21

print(r1, r2)