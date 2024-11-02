def sol(w1, w2):
    if w1 == "R" and w2 == "S":
        return True
    elif w1 == "S" and w2 == "P":
        return True
    elif w1 == "P" and w2 == "R":
        return True
    else:
        return False

n = int(input())
a = input()
b = input()
a_win, b_win = 0, 0

for i in range(n):
    if a[i] == b[i]:
        continue

    if sol(a[i], b[i]):
        a_win += 1
    else:
        b_win += 1

print("victory" if a_win > b_win else "defeat")
