while True:
    line = list(input().lower().split())
    # 탈출 조건
    if line[0] == "*":
        break
        
    first = line[0][0]
    flag = True
    # flag를 통해 검사
    for el in line[1:]:
        if first != el[0]:
            flag = False
            break
    print("Y" if flag else "N")