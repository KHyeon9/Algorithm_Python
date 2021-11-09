from sys import stdin
h, m, s = map(int, stdin.readline().split())
q = int(stdin.readline())
for i in range(q):
    time = list(map(int, stdin.readline().split()))
    if time[0] == 3:
        print(h, m, s)
    else:
        t = (h * 3600) + (m * 60) + s
        if time[0] == 1:
            t += time[1]
        else:
            t -= time[1]
        if t < 0:
            t += 24 * 3600
        t %= 24 * 3600
        h = t // 3600
        t %= 3600
        m = t // 60
        s = t % 60