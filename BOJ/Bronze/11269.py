word = "PER"
s = input()
res = 0

for i in range(len(s)):
    if s[i] != word[i % 3]:
        res += 1
print(res)