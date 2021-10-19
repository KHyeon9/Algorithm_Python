X, Y, Z = list(map(int, input().split()))

if X == Y == Z:
    print("2")

elif X ** 2 + Y ** 2 == Z ** 2 or X ** 2 + Z ** 2 == Y ** 2 or Y ** 2 + Z ** 2 == X ** 2:
    print("1")

else:
    print("0")