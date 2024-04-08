vowels = "aeiou"
s = input()
res = s

for i in range(len(s) - 1, -1, -1):
    if s[i].lower() in vowels:
        res = s[:i + 1] + "ntry"
        break
print(res)