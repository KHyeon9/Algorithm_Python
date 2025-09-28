flag = True

for _ in range(int(input())):
    n = int(input())

    if n < 48:
        flag = False

print(flag)
