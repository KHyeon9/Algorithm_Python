res = []

for _ in range(3):
    s = input()
    res.append(s[0])

print("GLOBAL" if sorted(res) == ['k', 'l', 'p'] else "PONIX")
