arr = [1, 2]
n = int(input())
for i in range(2, n):
    arr.append((arr[-2] + arr[-1]) % 15746)
print(arr[n - 1])