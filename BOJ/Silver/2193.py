arr = [1, 1]
n = int(input())
for i in range(2, n):
    arr.append(arr[i - 2] + arr[i - 1])
print(arr[-1])