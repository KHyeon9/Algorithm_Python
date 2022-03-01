a, b = map(int, input().split())
cnt = 0
num = 1
arr = []
while len(arr) != b:
    if num > arr.count(num):
        arr.append(num)
    else:
        num += 1
    cnt += 1
arr = arr[a - 1:b]
print(sum(arr))