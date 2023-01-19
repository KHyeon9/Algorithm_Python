a, b, c, d = map(int, input().split())
if a * b == c * d:
    print("E")
    exit()
print("M" if a * b > c * d else "P")