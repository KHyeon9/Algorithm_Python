vowels = ["a", "e", "i", "o", "u"]
ns = ["n", "s"]
s = input()
res = -1

if s[-1] not in vowels and s[-1] not in ns:
    for i in range(len(s) - 1, -1, -1):
        if s[i] in vowels:
            res = i + 1
            break
else:
    cnt = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] in vowels:
            cnt += 1
        if cnt == 2:
            res = i + 1
            break

print(res)
