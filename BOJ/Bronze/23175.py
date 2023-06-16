m = int(input())
sequence = list(map(int, input().split()))
res = []
pointer, cnt = 0, 0
for n in sequence:
    if pointer != n:
        pointer = n
        cnt = 1
    if cnt == pointer:
        res.append(n)
        pointer, cnt = 0, 0
    if pointer == n:
        cnt += 1
print(*res)