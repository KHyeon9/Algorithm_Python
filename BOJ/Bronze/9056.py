for _ in range(int(input())):
    a, b = input().split()
    a_set = set(a)
    b_set = set(b)
    flag = True
    if len(a_set) != len(b_set):
        flag = False
    else:
        for el in a_set:
            if el not in b_set:
                flag = False
    print("YES" if flag else "NO")