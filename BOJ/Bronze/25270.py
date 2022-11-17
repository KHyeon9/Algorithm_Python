def sol(x):
    if x % 100 == 99:
        return True
    return False


n = int(input())
if 1 <= n <= 98:
    print(99)
    exit()
idx = 1

while 1:
    if sol(n + idx):
        print(n + idx)
        break
    if sol(n - idx):
        print(n - idx)
        break

    idx += 1

