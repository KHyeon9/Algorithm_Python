n = int(input())

for i in range(1, n + 1):
    print(i)
    if i % 6 == 0 or i == n:
        cnt = 0
        print("Go!")
        continue


