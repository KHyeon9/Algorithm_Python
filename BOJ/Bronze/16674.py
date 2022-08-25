arr = [0] * 10
s = input()
for i in s:
    arr[int(i)] += 1

a = arr[0] + arr[1] + arr[2] + arr[8]

if a == sum(arr):
    if arr[0] == arr[1] == arr[2] == arr[8]:
        print(8)
    elif arr[0] != 0 and arr[1] != 0 and arr[2] != 0 and arr[8] != 0:
        print(2)
    else:
        print(1)
else:
    print(0)