n, d = map(int, input().split())
ud = {"d": "q", "b": "p", "q": "d", "p": "b"}
lr = {"d": "b", "b": "d", "q": "p", "p": "q"}

for _ in range(n):
    s = input()
    res = ""

    for w in s:
        if d == 1:
            res += ud[w]
        else:
            res += lr[w]

    print(res)