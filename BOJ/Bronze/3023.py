r, c = map(int, input().split())
arr = []
for _ in range(r):
    s = input()
    s += s[::-1]
    arr.append(s)
arr += arr[::-1]
a, b = map(int, input().split())
if arr[a - 1][b - 1] == '.':
    arr[a-1] = arr[a-1][:b-1] + '#' + arr[a-1][b:]
else:
    arr[a-1] = arr[a-1][:b-1] + '.' + arr[a-1][b:]
for i in arr:
    print(i)

