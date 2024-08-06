grade = {
    "A+": 4.5,
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0.0
}

s = input()
res = []
for i in range(len(s)):
    if s[i] == "+":
        continue

    if i + 1 < len(s) and s[i + 1] == "+":
        res.append(s[i:i+2])
    else:
        res.append(s[i])

total = sum([grade[g] for g in res])

print(total / len(res))