t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    r1 = n // m
    r2 = n % m

    print("You get %d piece(s) and your dad gets %d piece(s)." % (r1,  r2))