arr1 = []
arr2 = []

for _ in range(4):
    li = list(map(int, input().split()))
    arr1.append(li)

for i in range(4):
    line = []
    for j in range(4):
        line.append(arr1[j][i])
    arr2.append(line)

res = sum(arr1[0])
flag = True

for i in range(4):
    if res != sum(arr1[i]) or res != sum(arr2[i]):
        flag = False
        break

print("magic" if flag else "not magic")
