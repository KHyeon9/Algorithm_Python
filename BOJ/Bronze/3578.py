n = int(input())
if n == 0:
    print(1)
elif n == 1:
    print(0)
else:
    print('4' * (n % 2) + '8' * (n // 2))