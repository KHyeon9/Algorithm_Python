now =list(map(int, input().split()))
need = list(map(int, input().split()))
cookie = 0

for _ in range(int(input())):
    c, a = map(int, input().split())

    if c == 1:
        flag = True
        for i in range(4):
            if now[i] - need[i] * a < 0:
                flag = False
                break
        if flag:
            for i in range(4):
                now[i] -= need[i] * a
            cookie += a
            print(cookie)
        else:
            print("Hello, siumii")
    else:
        now[c - 2] += a
        print(now[c - 2])