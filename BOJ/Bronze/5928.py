D, H, M = list(map(int, input().split()))

T = D * 60 * 24 + H * 60 + M
T2 = 11 * 60 * 24 + 11 * 60 + 11
R = T - T2

if T<T2:
    print("-1")
else:
    print(R)
