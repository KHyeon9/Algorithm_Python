names = {
            "NLCS": "northlondo",
            "BHA" : "branksomeh",
            "KIS" : "koreainter",
            "SJA" : "stjohnsbur"
       }
alpa = "abcdefghijklmnopqrstuvwxyz"
line = input()
res = ""

for k, v in names.items():
    for i in range(26):
        temp = ""

        for ch in v:
            change_ch = ord(ch) + i
            temp += alpa[change_ch % 26]
        if temp == line:
            print(k)
            exit()


