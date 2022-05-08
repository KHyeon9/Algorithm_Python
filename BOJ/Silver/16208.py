n = int(input())
steel_stick = sorted(list(map(int, input().split())))
total_len = sum(steel_stick)
cost = 0
for i in steel_stick:
    total_len -= i
    cost += total_len * i
print(cost)