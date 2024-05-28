key = input()
message = input()
res = ""

for w in message:
    if w.isalpha():
        if w.isupper() and w.lower() in key:
            res += key[ord(w.lower()) - 97].upper()
        else:
            res += key[ord(w) - 97]
    else:
        res += w

print(res)