n1 = int(input())
n2 = input()
res = 0
print(n1)
print(n2)
for i in range(1, len(n2) + 1):
    temp = n1 * int(n2[-i])
    print(temp)
    res += temp * (10 ** (i - 1))
print(res)
