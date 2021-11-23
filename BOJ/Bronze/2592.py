arr = sorted([int(input()) for _ in range(10)])
print(sum(arr)//10)
MAX = 0
for i in arr:
    if arr.count(i) >= MAX:
        MAX = arr.count(i)
        r = i
print(r)

