while 1:
    a, b, c = map(int, input().split())
    A = a ** 2
    B = b ** 2
    C = c ** 2
    if a == 0 and b == 0 and c == 0:
        break
    if A + B == C or B + C == A:
        print("right")
    elif A + C == B:
        print("right")
    elif B + C == A:
        print("right")
    else:
        print("wrong")