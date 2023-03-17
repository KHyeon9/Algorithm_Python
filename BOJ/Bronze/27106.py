n = int(input())

change = 100 - n

print(change // 25, end=" ")

change %= 25

print(change // 10, end=" ")

change %= 10

print(change // 5, end=" ")

change %= 5

print(change)