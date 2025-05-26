n = int(input())
n_len = len(str(n))
res = 0

while True:
    n = n * 2
    if n_len < len(str(n)):
        print(res)
        break
    res += 1


