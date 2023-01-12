s = input()
p = 0
while p < len(s):
    print(s[p], end='')
    plus = ord(s[p]) - ord('A') + 1
    p += plus