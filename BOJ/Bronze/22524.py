right = "yuiophjklnm"
left = "qwertasdfgzxcvb"

while True:
    s = input()

    if s == "#":
        break
    res = 0
    hand = "r" if s[0] in right else "l"

    for w in s:
        if w in right and hand == "l":
            res += 1
            hand = "r"
        elif w in left and hand == "r":
            res += 1
            hand = "l"

    print(res)
