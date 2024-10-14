from sys import stdin

input = stdin.readline
score = sorted([float(input()) for _ in range(int(input()))])

for el in score[:7]:
    print(f"{el:.3f}")