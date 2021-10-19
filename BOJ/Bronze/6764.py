N = int(input())
N2 = int(input())
N3 = int(input())
N4 = int(input())

if N < N2 < N3 < N4:
    print("Fish Rising")

elif N > N2 > N3 > N4:
    print("Fish Diving")

elif N == N2 == N3 == N4:
    print("Fish At Constant Depth")
else:
    print("No Fish")