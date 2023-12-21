d1, m1, y1, n = map(int, input().split())
d2, m2, y2 = map(int, input().split())

res = (((y2 - y1) * 360) + ((m2 - m1) * 30) + (d2 - d1)) % 7 + n

print(res if res <= 7 else res - 7)