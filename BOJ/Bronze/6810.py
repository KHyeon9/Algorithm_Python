r = 91
for i in range(3):
    n = int(input())
    if i % 2 == 0:
        r += n
    else:
        r += n * 3
print(f'The 1-3-sum is {r}')