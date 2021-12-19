t = int(input())

for i in range(t):
    n = int(input())

    if n % 2 == 0:
        print("{} is even".format(n))
    else:
        print("{} is odd".format(n))