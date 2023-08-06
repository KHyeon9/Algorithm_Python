n = int(input())
work_list = [list(map(int, input().split())) for _ in range(3)]
res = []

for i in range(n):
    temp = []
    for j in range(3):
        temp.append(work_list[j][i])
    res.append(sorted(temp)[1])
print(*res)
