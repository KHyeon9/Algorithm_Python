for _ in range(int(input())):
    j, n = map(int, input().split())
    box = []
    cnt = 0
    for _ in range(n):
        a, b = map(int, input().split())
        box.append(a * b)
    box.sort(reverse=True)
    for i in box:
        j -= i
        cnt += 1
        if j <= 0:
            print(cnt)
            break