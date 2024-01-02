n = int(input())
want_char = int(input())
all_char = list(map(int, input().split()))
res = 1
for char in all_char:
    if want_char <= char:
        res += 1

print(res)