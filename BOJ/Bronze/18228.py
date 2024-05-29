n = int(input())
ice = list(map(int, input().split()))
penguin = ice.index(-1)
left = min(ice[:penguin])
right = min(ice[penguin + 1:])

print(left + right)