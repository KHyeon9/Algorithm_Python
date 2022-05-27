n, m = map(int, input().split())
a, d = map(int, input().split())
sr, sc = map(int, input().split())
result = "NO..."
if sr == n and n % 2 == (d + 1) % 2:
    result = "YES!"
print(result)
