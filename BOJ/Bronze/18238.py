alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = input()
pointer = 0
res = 0

for w in s:
    left_val = pointer - alpa.index(w)
    right_val = alpa.index(w) - pointer
    if left_val < 0:
        left_val += 26
    else:
        right_val += 26
    res += min(left_val, right_val)
    pointer = alpa.index(w)
print(res)