n, l, k = map(int, input().split())
e, h = 0, 0
for _ in range(n):
    easy, hard = map(int, input().split())
    if hard <= l:
        h += 1
    elif easy <= l:
        e += 1
result = 140 * min(h, k)
if h < k:
    result += min(k - h, e) * 100
print(result)