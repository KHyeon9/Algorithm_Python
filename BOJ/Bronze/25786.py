n1 = input()
n2 = input()
n1_l, n2_l = len(n1), len(n2)

if n2_l > n1_l:
    n1 = (n2_l - n1_l) * '0' + n1
else:
    n2 = (n1_l - n2_l) * '0' + n2

res = ""

for i in range(max(n1_l, n2_l)):
    n1_i, n2_i = int(n1[i]), int(n2[i])
    if n1_i <= 2 and n2_i <= 2 or n1_i >= 7 and n2_i >= 7:
        res += "0"
        continue
    res += "9"

print(res)