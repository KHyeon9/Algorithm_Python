hiarc = "HIARC"
res = [0] * 5

n = int(input())
s = input()

for i in range(5):
    res[i] = s.count(hiarc[i])
print(min(res))