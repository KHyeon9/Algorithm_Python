n = int(input())
s = input()
ioi = "IOI"
position = 0

for w in s:
    if w == ioi[position]:
        position += 1
    if position == 3:
        break

print("Yes" if position == 3 else "No")

