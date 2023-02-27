n = int(input())
s = input()
coffee, wakeCnt = 0, 0

for i in s:
    if i == '1':
        coffee = 2
        wakeCnt += 1
    else:
        if coffee > 0:
            coffee -= 1
            wakeCnt += 1
print(wakeCnt)