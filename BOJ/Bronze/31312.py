n, a, b = map(int, input().split())
arr = [0] * (b + 1)
flag = True

for _ in range(n - 1):
    w = int(input())

    if w < a or w > b:
        flag = False

    arr[w] = 1

if flag:
    if arr[a] == 0 and arr[b] == 0:
        print(-1)
    elif arr[a] == 0:
        print(a)
    elif arr[b] == 0:
        print(b)
    else:
        for i in range(a, b + 1): print(i)
else:
    print(-1)