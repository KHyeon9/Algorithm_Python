s = input()
r = ''
for word in s:
    a = ord(word) - 3
    if a < 65:
        a += 26
    r += chr(a)
print(r)
