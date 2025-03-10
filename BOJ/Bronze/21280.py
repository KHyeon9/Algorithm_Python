n = int(input())
arr = list(map(int, input().split()))
now = arr[0]
res = [0, 0]
for el in arr[1:]:
    if now > el:
        res[0] += now - el
    elif now < el:
        res[1] += el - now
    now = el
print(*res)