x = int(input())
m = int(input())
for i in range(1, 100001):
    if (m * i + 1) % x == 0:
        print((m * i + 1) // x)
        break
    i += 1
else:
    print("No such integer exists.")