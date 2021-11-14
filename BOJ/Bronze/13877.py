for _ in range(int(input())):
    k, n = input().split()
    if int(max(list(n))) > 7:
        print(int(k), 0, int(n), int(n, 16))
    else:
        print(int(k), int(n, 8), int(n), int(n, 16))
