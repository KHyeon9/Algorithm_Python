arr = []
for i in range(3):
    m, w = map(int, input().split())
    m *= 10
    w *= 10
    if m >= 5000:
        m -= 500
    arr.append(w / m)
if arr[0] == max(arr):
    print('S')
elif arr[1] == max(arr):
    print('N')
else:
    print('U')