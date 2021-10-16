a = list(map(int, input().split()))
b = list(map(int, input().split()))
r1 = b[0] - a[2]
r2 = b[1] // a[1]
r3 = b[2] - a[0]
print(r1, r2, r3)