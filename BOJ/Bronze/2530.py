H, M, S = list(map(int, input().split()))

P = int(input())

S += P

if S >= 60:
    M += S // 60
    S %= 60
    
    if M >= 60:
        H += M // 60
        M %= 60
        
        if H >= 24:
            H %= 24

print(H, M, S)