n = int(input())
f = n % 8

if f == 1:
    print(1)

elif f == 0 or f == 2:
    print(2)

elif f == 3 or f == 7:
    print(3)

elif f == 4 or f == 6:
    print(4)

else:
    print(5)