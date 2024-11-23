def sol(arr, cnt, now, c):
    if len(res[now]) < cnt:
        res[now] += c
    else:
        if len(res[(now + 1) % 3]) < cnt:
            res[(now + 1) % 3] += c
        else:
            res[(now + 2) % 3] += c

n, k = map(int, input().split())
s = input()

res = ["", "", ""]

for el in s:
    if el == "s":
        sol(res, k, 0, el)
    elif el == "r":
        sol(res, k, 1, el)
    else:
        sol(res, k, 2, el)

for el in res:
    print(el)