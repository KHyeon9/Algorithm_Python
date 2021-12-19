t = int(input())

for i in range(t):
    v, e = list(map(int, input().split()))

    r = 2 - v + e
    
    print(r)