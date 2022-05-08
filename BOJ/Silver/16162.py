n, a, d = map(int, input().split())
high_note = list(map(int, input().split()))
level = 0

for i in range(n):
    if high_note[i] == a + (d * level):
        level += 1
print(level)

