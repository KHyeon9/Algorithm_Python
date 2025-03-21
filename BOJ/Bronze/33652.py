n = int(input())
off = []

for _ in range(n):
    m, o = map(int, input().split())
    if o == 0:
        off.append(m)

print(sorted(off)[0] if len(off) > 0 else -1)