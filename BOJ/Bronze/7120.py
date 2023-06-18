s = input()
res = ""

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        res += s[i]
print(res + s[-1])
