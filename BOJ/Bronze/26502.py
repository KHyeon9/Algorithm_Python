replacement = "aeiouy"

for _ in range(int(input())):
    s = input()
    res = ""
    for w in s:
        if w.lower() in replacement:
            idx = (replacement.find(w.lower()) + 1) % len(replacement)
            if w.isupper():
                res += replacement[idx].upper()
            else:
                res += replacement[idx]
            continue
        res += w
    print(res)