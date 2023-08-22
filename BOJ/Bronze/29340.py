n1 = input()
n2 = input()
res = ""

for i in range(len(n1)):
    if int(n1[i]) > int(n2[i]):
        res += n1[i]
    else:
        res += n2[i]
print(res)