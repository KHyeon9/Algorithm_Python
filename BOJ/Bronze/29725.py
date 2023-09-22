b_ch = {"k": 0, "p": 1, "n": 3, "b": 3, "r": 5, "q": 9}
w_ch = {"K": 0, "P": 1, "N": 3, "B": 3, "R": 5, "Q": 9}

b_total, w_total = 0, 0

for _ in range(8):
    line = input()

    for w in line:
        if w in b_ch:
            b_total += b_ch[w]
        elif w in w_ch:
            w_total += w_ch[w]


print(w_total - b_total)
