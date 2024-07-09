n = int(input())
s = input()
arr, cnt = [0], 1

for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        cnt += 1
    else:
        arr.append(cnt)
        cnt = 1
arr.append(cnt)

res = 0

for i in range(1, len(arr)):
    res = max(res, min(arr[i - 1], arr[i]))

print(res * 2)