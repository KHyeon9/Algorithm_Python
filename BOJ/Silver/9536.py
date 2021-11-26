t = int(input())
for _ in range(t):
    s = input().split()
    arr = []
    result = []
    while 1:
        s2 = input().split()
        if s2[-1] == 'say?':
            break
        arr.append(s2[2])
    for i in s:
        if i not in arr:
            result.append(i)
    print(*result)

