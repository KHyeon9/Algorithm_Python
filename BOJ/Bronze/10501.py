arr = []
res = 0

while True:
    try:
        arr.append(len(input()))
    except:
        break

max_len = max(arr)

for el in arr[:-1]:
    res += (max_len - el) ** 2

print(res)
