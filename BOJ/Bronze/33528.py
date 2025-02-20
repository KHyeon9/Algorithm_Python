alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
line = input()

for i in range(26):
    res = ""
    for w in line:
        res += alpa[(ord(w) - 65 - i) % 26]

    print(res)