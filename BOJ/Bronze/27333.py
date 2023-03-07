n = int(input())
s = list(input())

for i in range(n - 1):
    if s[i] in ['j', 'o', 'i'] and s[i] == s[i + 1]:
        s[i], s[i + 1] = s[i].upper(), s[i + 1].upper()
print(*s, sep='')