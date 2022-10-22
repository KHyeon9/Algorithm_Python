n = int(input())
s = list(input())
for i in range(n):
    if s.count('s') == s.count('t'):
        break
    s.pop(0)
print(*s, sep='')