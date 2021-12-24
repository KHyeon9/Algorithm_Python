n = input().split('-')
arr = []
for i in n:
    r_plus = 0
    n2 = i.split('+')
    for j in n2:
        r_plus += int(j)
    arr.append(r_plus)
print(arr[0] * 2 - sum(arr))