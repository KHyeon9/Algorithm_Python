n = int(input())
s = input()
flags = [False, False, False, False]
sp_text = "!@#$%^&*()-+"

for w in s:
    if w.isdigit():
        flags[0] = True
    if w.islower():
        flags[1] = True
    if w.isupper():
        flags[2] = True
    if w in sp_text:
        flags[3] = True

false_count = flags.count(False)
res = max(0, 6 - len(s) - false_count) + false_count
print(res)