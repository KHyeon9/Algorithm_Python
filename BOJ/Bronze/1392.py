n, q = map(int, input().split())
time = [0] * (n + 1)
for i in range(1, n + 1):
    time[i] = int(input())
for _ in range(q):
    t = int(input())
    total = 0
    for i in range(1, n + 1):
        total += time[i - 1]
        if total <= t < total + time[i]:
            print(i)
            break