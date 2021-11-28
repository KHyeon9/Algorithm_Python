t = int(input())

for i in range(t):
    s = int(input())
    n = int(input())
    r = 0

    for j in range(n):
        n_list = list(map(int, input().split()))
        r += n_list[0] * n_list[1]

    print(r + s)