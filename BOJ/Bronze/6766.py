k = int(input())
s = list(input())

for i in range(len(s)):
    z = 3 * i + k + 3
    w = (ord(s[i]) - ord('A') - z) % 26 + ord('A')
    s[i] = chr(w)

print(*s, sep='')