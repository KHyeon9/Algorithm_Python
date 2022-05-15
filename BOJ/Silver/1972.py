while 1:
    s = input()
    if s == '*':
        break
    flag = True
    for i in range(1, len(s)):
        arr = []
        for j in range(len(s) - i):
            line = s[j] + s[j + i]
            j += i
            arr.append(line)
        if len(arr) != len(set(arr)):
            flag = False
            break

    if flag:
        print(f"{s} is surprising.")
    else:
        print(f"{s} is NOT surprising.")