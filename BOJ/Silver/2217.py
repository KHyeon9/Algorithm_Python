n = int(input())
rope = sorted([int(input()) for _ in range(n)], reverse=True)
m = 0
for i in range(n):

    if m < rope[i] * (i + 1):
        m = rope[i] * (i + 1)
print(m)


