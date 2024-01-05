n, m, k = map(int, input().split())
download = sorted(list(map(int, input().split())), reverse=True)
s = sum(download)
now = sum(download[:m + k])
res = now / s * 100

print(f"{res:.6f}")