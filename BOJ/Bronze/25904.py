n, x = map(int, input().split())
voice = list(map(int, input().split()))
idx = 0
while 1:
    if voice[idx % n] < x:
        print(idx % n + 1)
        break
    idx += 1
    x += 1
