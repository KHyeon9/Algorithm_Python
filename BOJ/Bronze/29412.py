light = list(map(int, input().split()))
t = int(input())
g, y, r = 0, 0, 0
time, idx = 0, 0

for i in range(t):
    if idx == 0:
        g += 1
    elif idx == 1:
        g += i % 2
    elif idx == 2:
        y += 1
    elif idx == 3:
        r += 1
    else:
        y += 1
        r += 1

    time += 1

    if time == light[idx]:
        idx = (idx + 1) % 5
        time = 0
print(r, y, g)