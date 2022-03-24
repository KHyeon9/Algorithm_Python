n = int(input())
arr = [input() for _ in range(n)]
flag = True
for i in range(n):
    s1 = arr[i]
    s2 = ''
    for j in range(n):
        s2 += arr[j][i]
    if s1 != s2:
        print("NO")
        break
else:
    print("YES")
