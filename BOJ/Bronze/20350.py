s = input()
transform = ""
for w in s[4:] + s[:4]:
    if w.isalpha():
        transform += str(ord(w) - 55)
    else:
        transform += w
print("correct" if int(transform) % 97 == 1 else "incorrect")
