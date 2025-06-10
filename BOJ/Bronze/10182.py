from math import log10

for _ in range(int(input())):
    line = list(input().split())
    res = -log10(float(line[2]))

    if line[0] == "OH":
        res = 14 - res

    print(f"{res:.2f}")