n = int(input())
num = 2 ** n
print(bin((num * (num - 1)) // 2)[2:])