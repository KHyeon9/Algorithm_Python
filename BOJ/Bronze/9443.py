al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
input_arr = set([input()[0] for _ in range(int(input()))])
res = 0

for i in range(26):
    if al[i] not in input_arr:
        break
    res += 1

print(res)
