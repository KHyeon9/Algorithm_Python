n, a, b = map(int, input().split())
praise, blame = 1, 1

for _ in range(n):
    praise += a
    blame += b

    if praise < blame:
        praise, blame = blame, praise

    if praise == blame:
        blame -= 1

print(praise, blame)