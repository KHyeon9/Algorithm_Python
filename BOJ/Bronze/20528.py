n = int(input())
word_relay = list(input().split())
res = 1

for i in range(1, n):
    if word_relay[i - 1][-1] != word_relay[i][0]:
        res = 0
        break
print(res)