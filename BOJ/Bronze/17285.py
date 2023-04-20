s = input()

key = ord(s[0]) ^ ord("C")
res = ""

for w in s:
    res += chr(ord(w) ^ key)
print(res)