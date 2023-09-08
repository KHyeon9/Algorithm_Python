product = {"H": 1, "C": 12, "N": 14, "O": 16}

s = input()
index, res = 0, 0
while len(s) > index:
    if index < len(s) - 1 and s[index + 1].isdigit():
        res += product[s[index]] * int(s[index + 1])
        index += 2
    else:
        res += product[s[index]]
        index += 1
print(res)