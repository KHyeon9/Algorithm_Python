for _ in range(int(input())):
    w, k = map(int, input().split())
    if w == k == 1:
        print(0)
        continue
    print(w * k // 2)