def sol(c1, c2):
    if c1 == 'A' and c2 == 'A':
        return 'A'
    if c1 == 'A' and c2 == 'G':
        return 'C'
    if c1 == 'A' and c2 == 'C':
        return 'A'
    if c1 == 'A' and c2 == 'T':
        return 'G'

    if c1 == 'G' and c2 == 'A':
        return 'C'
    if c1 == 'G' and c2 == 'G':
        return 'G'
    if c1 == 'G' and c2 == 'C':
        return 'T'
    if c1 == 'G' and c2 == 'T':
        return 'A'

    if c1 == 'C' and c2 == 'A':
        return 'A'
    if c1 == 'C' and c2 == 'G':
        return 'T'
    if c1 == 'C' and c2 == 'C':
        return 'C'
    if c1 == 'C' and c2 == 'T':
        return 'G'

    if c1 == 'T' and c2 == 'A':
        return 'G'
    if c1 == 'T' and c2 == 'G':
        return 'A'
    if c1 == 'T' and c2 == 'C':
        return 'G'
    if c1 == 'T' and c2 == 'T':
        return 'T'


l = int(input())
s = list(map(str, input()))
i = 0
while i != l:
    i += 1
    r = sol(s[l-i], s[l-i-1])
    if len(s) != 1:
        s.pop()
        s.pop()
        s.append(r)
    else:
        break
print(s[0])




