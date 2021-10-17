H, M = list(map(int, input().split()))

P = int(input())

M = M + P

if M >= 60:
    Over = M // 60
    M = M % 60
    H += Over

    if H >= 24:
        H = H % 24

print(H, M)
