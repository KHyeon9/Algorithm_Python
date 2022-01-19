arr = sorted(list(map(int, input().split())))
if arr[0] == arr[1] or arr[1] == arr[2] or arr[0] + arr[1] == arr[2]:
    print('S')
else:
    print('N')

