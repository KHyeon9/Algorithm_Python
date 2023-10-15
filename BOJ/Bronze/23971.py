from math import ceil

h, w, n, m = map(int, input().split())

res_h = ceil(h / (n + 1))
res_w = ceil(w / (m + 1))

print(res_h * res_w)