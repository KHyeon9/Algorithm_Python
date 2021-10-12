a, b = input().split()

c = list(map(int, input().split()))

d = int(a) * int(b)

for i in c:
    print(i-d, end=' ')