dic = {}
cnt = 0
penalty = 0

while True:
    problem = list(input().split())

    if problem[0] == '-1':
        break

    if problem[2] == "right":
        cnt += 1
        penalty += int(problem[0])
        if problem[1] in dic:
            penalty += dic[problem[1]] * 20
        continue

    if problem[1] not in dic:
        dic[problem[1]] = 1
    else:
        dic[problem[1]] += 1

print(cnt, penalty)


