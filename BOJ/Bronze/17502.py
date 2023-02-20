import math
n = int(input())
s = list(input())
n = math.ceil(n / 2)
for i in range(n):
    if s[i] == s[-i - 1] == '?':
        s[i] = 'a'
        s[-i - 1] = 'a'
    elif s[i] == '?':
        s[i] = s[-i - 1]
    elif s[-i - 1] == '?':
        s[-i - 1] = s[i]
print(*s,sep='')