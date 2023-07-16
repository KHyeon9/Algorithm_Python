res_list = []
pi = 3.14159

for _ in range(int(input())):
    line = list(input().split())

    if line[0] == "C":
        r, h = float(line[1]), float(line[2])
        res = (1 / 3) * pi * (r ** 2) * h
        res_list.append(res)
    elif line[0] == "L":
        r, h = float(line[1]), float(line[2])
        res = pi * (r ** 2) * h
        res_list.append(res)
    else:
        r = float(line[1])
        res = (4 / 3) * pi * (r ** 3)
        res_list.append(res)

print("%.3f" % max(res_list))
