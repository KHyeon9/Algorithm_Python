def instruction(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    return -1


four_directions = ["N", "E", "S", "W"]
t = 0

for _ in range(10):
    n = int(input())
    t += instruction(n)

print(four_directions[t % 4])
