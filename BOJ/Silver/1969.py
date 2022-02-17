n, m = map(int, input().split())
dna = [input() for _ in range(n)]
result = ''
cnt = 0
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        if dna[j][i] == 'A':
            a += 1
        elif dna[j][i] == 'C':
            c += 1
        elif dna[j][i] == 'G':
            g += 1
        else:
            t += 1
    MAX = max(a, c, g, t)
    if MAX == a:
        result += 'A'
        cnt += c + g + t
    elif MAX == c:
        result += 'C'
        cnt += a + g + t
    elif MAX == g:
        result += 'G'
        cnt += a + c + t
    else:
        result += 'T'
        cnt += a + c + g
print(result)
print(cnt)
