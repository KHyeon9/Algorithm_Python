for _ in range(int(input())):
    line = input()
    rev, flag = 0, False
    num = 0

    for w in line:
        if not flag and w == "!":
            rev += 1
        elif w.isdigit():
            flag = True
            num = int(w)
            break

    if line[-1] == "!":
        num = 1

    if num == 0:
        print(0 if rev % 2 == 0 else 1)
    else:
        print(0 if rev % 2 == 1 else 1)
