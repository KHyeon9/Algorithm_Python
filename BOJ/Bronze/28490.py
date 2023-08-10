max_fr = 0
for _ in range(int(input())):
    h, w = map(int, input().split())
    max_fr = max(max_fr, h * w)

print(max_fr)