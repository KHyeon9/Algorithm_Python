t = int(input())

for i in range(t):
    n = list(map(int, input().split()))
    r = 100
    s = 0

    for j in range(len(n)):
        if n[j] % 2 == 0:
            s += n[j]

            if r > n[j]:
                r = n[j]

    print(s, r)
