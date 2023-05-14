mosq = {'B': 'v', 'E': 'ye', 'H': 'n', 'P': 'r', 'C': 's',
        'Y': 'u', 'X': 'h'}

s = input()
res = ""

for w in s:
    if w in mosq:
        res += mosq[w]
        continue
    res += w.lower()
print(res)
