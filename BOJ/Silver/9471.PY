n = int(input())
for i in range(n):
    n, m = map(int, input().split())
    arr = [0, 1, 1]
    while 1:
        r = arr[-1] + arr[-2]
        arr.append(r % m)
        if arr[-1] == 1 and arr[-2] == 1:
            break
    print(n, len(arr) - 3)
