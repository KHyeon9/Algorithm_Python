N = int(input()) + 1

gifts = []

for k in range(1, N):
    gifts.append((N - k) * k)

for count in gifts:
    print(count)
