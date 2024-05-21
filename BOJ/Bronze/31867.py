odd, even = 0, 0
n = int(input())

for n in input():
    if int(n) % 2 != 0:
        odd += 1
    else:
        even += 1

if odd < even:
    print(0)
elif odd > even:
    print(1)
else:
    print(-1)