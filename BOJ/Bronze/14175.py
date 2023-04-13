n, m, k = map(int, input().split())
res = []

for _ in range(n):
    line = input()
    res_line = ""
    for i in line:
        res_line += i * k
    for i in range(k):
        res.append(res_line)
for i in res:
    print(i)