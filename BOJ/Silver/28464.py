from sys import stdin

n = int(stdin.readline())
french_fries = sorted(list(map(int, stdin.readline().split())))
sung, park = sum(french_fries[:n // 2]), sum(french_fries[n // 2:])

print(sung, park)

