t1 = int(input())
t2 = int(input())
r = 2
while t1 - t2 >= 0:
    sumac = t1 - t2
    t1 = t2
    t2 = sumac
    r += 1
print(r)