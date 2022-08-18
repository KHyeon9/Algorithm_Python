for _ in range(int(input())):
    s1, s2 = input().split()
    s1 = sorted(list(s1))
    s2 = sorted(list(s2))
    if s1 == s2:
        print("Possible")
    else:
        print("Impossible")