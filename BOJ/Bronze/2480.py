A, B, C = list(map(int, input().split()))

if A == B == C:
    print(10000 + A * 1000)

elif A == B != C:
    print(1000 + 100 * A)

elif A == C != B:
    print(1000 + 100 * A)

elif B == C != A:
    print(1000 + 100 * B)

else:
    print(100 * max(A, B, C))