N1, N2 = list(map(int, input().split()))

A = N1 + N2
B = N1 - N2

if A % 2 != 0 and B % 2 != 0:
    print("-1")

else:
    if A // 2 >= 0 and B // 2 >= 0:
        print(A // 2, B // 2)

    else:
        print("-1")