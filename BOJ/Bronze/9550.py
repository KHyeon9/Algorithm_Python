t = int(input())

for i in range(t):
    n, k = list(map(int, input().split()))
    num = list(map(int, input().split()))
    r = 0

    for j in range(n):
        r += num[j] // k

    print(r)