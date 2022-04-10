num = sorted(list(map(int, input().split())))
arr = []
for i in range(num[0] + 1, num[1]):
    arr.append(i)
print(len(arr))
print(*arr, sep=' ')