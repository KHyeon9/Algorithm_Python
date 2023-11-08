n = int(input())
w_li = list(input().split())
res = w_li[0][0]
p = len(w_li[0])

for w in w_li[1:]:
    if len(w) >= p:
        res += w[p - 1]
    else:
        res += " "
    p = len(w)
print(res)