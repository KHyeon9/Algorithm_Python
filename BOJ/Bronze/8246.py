A, B, K = list(map(int, input().split()))

R1 = A // K
R2 = B // K

if A < K or B < K:
    print("0")

elif (R1 - 2) < 0 or R2 - 2 < 0:
    print(R1 * R2)

else:
    print(R1 * R2 - (R1 - 2) * (R2 - 2))