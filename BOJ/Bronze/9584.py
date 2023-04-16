res = []

scan = input()

for _ in range(int(input())):
    code = input()
    flag = True
    for i in range(len(scan)):
        if scan[i] == '*':
            continue

        if scan[i] != code[i]:
            flag = False
            break
    if flag:
        res.append(code)
print(len(res))
for i in res:
    print(i)