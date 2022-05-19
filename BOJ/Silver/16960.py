n, m = map(int, input().split())
switchs = []
lamps = [0] * (m + 1)

for _ in range(n):
    switch = list(map(int, input().split()))[1:]
    switchs.append(switch)
    for i in switch:
        lamps[i] += 1

for s in switchs:
    flag = True

    for on in s:
        lamps[on] -= 1
    for i in lamps[1:]:
        if i < 1:
            flag = False

    if flag:
        print(1)
        exit()

    for i in s:
        lamps[i] += 1
print(0)