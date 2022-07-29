flag = False

for _ in range(int(input())):
    s = input()
    if s in "anj":
        flag = True
print("뭐야;" if flag else "뭐야?")