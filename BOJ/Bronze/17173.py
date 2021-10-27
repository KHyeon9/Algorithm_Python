n, m = map(int, input().split())
k = list(map(int, input().split()))
arr = []
for i in k:
    c = 1
    num = i
    while 1:
        arr.append(num)
        num = i * c
        c += 1
        if num > n:
            break
arr = set(arr)
print(sum(arr))