arr = [0]

for i in range(1, int(input()) + 1):
    arr.append(arr[i - 1] + i)
print(sum(arr))
