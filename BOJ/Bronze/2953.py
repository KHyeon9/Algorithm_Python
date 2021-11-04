win_point = 0
p = 0

for i in range(5):
    n = list(map(int, input().split()))
    p = 0

    for j in range(4):
        p += n[j]

    if p > win_point:
        win_point = p
        win = i

print(win + 1, win_point)