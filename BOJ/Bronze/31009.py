n = int(input())

region_list = {}

for _ in range(n):
    region, cost = input().split()
    cost = int(cost)
    region_list[region] = cost

jinju_cost = region_list["jinju"]
expensive_count = 0

for region in region_list:
    if jinju_cost < region_list[region]:
        expensive_count += 1

print(jinju_cost)
print(expensive_count)