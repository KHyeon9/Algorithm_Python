t = int(input())

for i in range(t):
    a, n = map(int, input().split())
    a = str(bin(a))
    r = a.count("1")
    if r % 2 == 1 and n == 1:
        print("Valid")
    elif r % 2 == 1 and n == 0:
        print("Corrupt")
    elif r % 2 == 0 and n == 0:
        print("Valid")
    else:
        print("Corrupt")