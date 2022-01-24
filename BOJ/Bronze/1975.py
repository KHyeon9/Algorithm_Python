from sys import stdin
for _ in range(int(input())):
    n = int(stdin.readline())
    cnt = 0
    for i in range(2, n + 1):
        num = n
        while num:
            if num % i == 0:
                cnt += 1
                num //= i
            else:
                break
    print(cnt)