n = int(input())
text1, text2 = input(), input()
res = 0

for i in range(n):
    if text1[i] == text2[i]:
        res += 1

print(res)