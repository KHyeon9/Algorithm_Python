l_list = sorted(list(map(int, input().split())), reverse=True)
res = 0

for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            if l_list[i] < l_list[j] + l_list[k]:
                res += 1

print(res)
