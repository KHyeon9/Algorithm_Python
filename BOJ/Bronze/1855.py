k = int(input())
s = input()
arr = []
for i in range(len(s) // k):
    if i % 2 == 0:
        arr.append(s[i * k:i * k + k])
    else:
        arr.append(s[i * k:i * k + k][::-1])
for i in range(k):
    for j in range(len(arr)):
        print(arr[j][i], end='')
