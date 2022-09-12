year = int(input())

while 1:
    year += 1
    n = str(year)
    flag = True
    for j in n:
        if n.count(j) >= 2:
            flag = False
            break
    if flag:
        print(year)
        break