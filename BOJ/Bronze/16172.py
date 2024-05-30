s = input()
k = input()
total = "".join([w for w in s if w.isalpha()])

print(1 if k in total else 0)