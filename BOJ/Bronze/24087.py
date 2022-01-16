from math import ceil
s = int(input())
a = int(input())
b = int(input())
if s >= a:
    print(250 + ceil((s - a) / b) * 100)
else:
    print(250)
