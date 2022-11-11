n = int(input())
arr = [0] * n
for i in range(n):
    gift = int(input())
    arr[gift - 1] = i + 1
for i in arr:
    print(i)