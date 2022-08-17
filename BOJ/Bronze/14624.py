n = int(input())
if n % 2 == 0:
    print("I LOVE CBNU")
elif n == 1:
    print("*")
else:
    space = n // 2
    print("*" * n)
    print(" " * space + "*")
    while space:
        space -= 1
        print(" " * space + "*" + " " * (n - space * 2 - 2) + "*")
