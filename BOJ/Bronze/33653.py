s = input()
n = int(input())
s_list = list(input().split())
res = 0

for el in s_list:
    for i in range(len(el) - len(s) + 1):
        if el[i:i + len(s)] == s:
            res += 1

print(res)
