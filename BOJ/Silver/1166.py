n, l, w, h = map(int, input().split())
start, end = 0, min(l, w, h)
for _ in range(100):
    mid = (start + end) / 2
    a = (l // mid) * (w // mid) * (h // mid)
    if a < n:
        end = mid
    else:
        start = mid
print('%.10f' % start)