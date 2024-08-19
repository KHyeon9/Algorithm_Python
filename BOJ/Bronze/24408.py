first_num = -1

for _ in range(int(input())):
    n = int(input())

    if first_num == -1:
        first_num = n
        continue

    if n % first_num == 0:
        print(n)
        first_num = -1

