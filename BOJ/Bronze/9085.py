t = int(input())

for i in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))
    r = 0

    for j in range(n):
        r += n_list[j]

    print(r)