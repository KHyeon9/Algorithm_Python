max_s, f, tf, sf = 0, 0, 0, 0

for i in range(1, int(input()) + 1):
    t, s = map(int, input().split())

    if s > max_s:
        max_s = s
        f = i
        tf = t
        sf = s

if sf == 0:
    print(0)
else:
    print(tf + (f - 1) * 20)