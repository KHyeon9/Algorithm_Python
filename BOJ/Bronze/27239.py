n = int(input())
al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
r1 = al[n % 8 - 1]
r2 = (n - 1) // 8 + 1
print(r1 + str(r2))