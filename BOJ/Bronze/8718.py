x, k = list(map(int, input().split()))

R = k + k * 2 + k * 4
R2 = k / 2 + k + k * 2
R3 = k / 4 + k / 2 + k

if R <= x:
    print(round(R * 1000))

elif R2 <= x:
    print(round(R2 * 1000))

elif R3 <= x:
    print(round(R3 * 1000))

else:
    print("0")