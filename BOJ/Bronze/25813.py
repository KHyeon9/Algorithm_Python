s = input()

uIndex = s.find("U")
fIndex = s.rfind("F")
res = ""

for i in range(len(s)):
    if i < uIndex or i > fIndex:
        res += "-"
    elif i == uIndex or i == fIndex:
        res += s[i]
    else:
        res += "C"
print(res)