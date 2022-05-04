n = int(input())
drink = sorted(list(map(int, input().split())), reverse=True)
mix = drink[0]
for i in range(1, n):
    mix += drink[i] / 2
print(mix)

