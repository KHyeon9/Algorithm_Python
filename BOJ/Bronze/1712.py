A, B, C = list(map(int, input().split()))

if B < C:
    print(A // (C - B) + 1)
    
elif B >= C:
    print("-1")