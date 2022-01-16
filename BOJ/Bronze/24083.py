S = [int(input()) for _ in range(2)]
if sum(S) % 12 == 0:
    print(12)
else:
    print(sum(S) % 12)