r, f = map(int, input().split())
res = round(f / r) % 2
print("up" if res == 0 else "down")