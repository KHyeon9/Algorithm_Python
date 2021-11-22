from sys import stdin
a, b = stdin.readline().split()
Sum_a, Sum_b = 0, 0
for i in a:
    Sum_a += int(i)
for i in b:
    Sum_b += int(i)
print(Sum_a * Sum_b)


