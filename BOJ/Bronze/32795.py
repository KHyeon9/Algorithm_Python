for _ in range(int(input())):
    a = input()
    b = input()
    flag = True

    for w in b:
        if w not in a:
            flag = False
            break

    print("YES" if flag else "NO")