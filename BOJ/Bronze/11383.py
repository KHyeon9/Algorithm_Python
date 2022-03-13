n, m = map(int, input().split())
words = [input() for _ in range(n)]
words2 = [input() for _ in range(n)]
result = True
for i in range(n):
    s = ''
    for j in words[i]:
        s += j * 2
    if s != words2[i]:
        result = False

print("Eyfa" if result else "Not Eyfa")



