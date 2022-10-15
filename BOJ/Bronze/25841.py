start, end, n = map(int, input().split())
n = str(n)
cnt = 0
for i in range(start, end + 1):
    i = str(i)
    if n in i:
        cnt += i.count(n)
print(cnt)

