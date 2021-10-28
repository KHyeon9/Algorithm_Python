k = int(input())
m = 25 + k * 0.01
r = min(max(m, 100), 2000)
print("%.2f" % r)