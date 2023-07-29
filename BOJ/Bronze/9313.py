while True:
    n = int(input())
    if n == -1:
        break
    n_bin = bin(n)[2:]
    n_rev = ('0' * (32 - len(n_bin)) + n_bin)[::-1]
    print(int(n_rev, 2))
