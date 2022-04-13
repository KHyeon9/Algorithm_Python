n, p = map(int, input().split())
num = n
arr = []
while 1:
    num = num * n % p
    if num in arr:
        print(len(arr) - arr.index(num))
        break
    arr.append(num)


