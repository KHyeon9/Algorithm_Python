D, C = 10, 26
s = input()
if s[0] == 'd':
    r = 10
else:
    r = 26
for i in range(1, len(s)):
    if s[i] == 'c':
        if s[i - 1] == 'c':
            r *= 25
        else:
            r *= 26
    else:
        if s[i - 1] == 'd':
            r *= 9
        else:
            r *= 10

print(r)
