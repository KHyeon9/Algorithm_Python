bord = input()
bord = bord.replace("XXXX", "AAAA")
bord = bord.replace("XX", "BB")

print(bord if 'X' not in bord else -1)
