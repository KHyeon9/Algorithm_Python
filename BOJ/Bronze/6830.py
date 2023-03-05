arr = []

while 1:
    try:
        val = list(input().split())
        val[1] = int(val[1])
        arr.append(val)
    except EOFError:
        break

arr.sort(key=lambda x: x[1])
print(arr[0][0])

