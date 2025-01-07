A, B, C = input().split()

if A == B == C:
    result = A + B + C
elif B == C:
    result = A + B + C + A
elif A == C:
    result = A + B + A
else:
    result = A + B + C + B + A

print(result)