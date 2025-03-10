a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
h, m, s = map(int, input().split())

total_seconds = h * b1 * c1 + m * c1 + s
res_h = total_seconds // (b2 * c2) % a2
res_m = total_seconds % (b2 * c2) // c2
res_s = total_seconds % c2
print(res_h, res_m, res_s)