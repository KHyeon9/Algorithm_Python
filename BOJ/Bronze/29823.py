input()
n_s, w_e = 0, 0
for el in input():
    if el == "N":
        n_s += 1
    elif el == "S":
        n_s -= 1
    elif el == "W":
        w_e += 1
    else:
        w_e -= 1

print(abs(n_s) + abs(w_e))

