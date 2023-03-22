s = input()

vowel = "aeiou"
flag = 1

for i in range(1, len(s)):
    if s[i] in vowel and s[i - 1] in vowel:
        flag = 0
        break
    if s[i] not in vowel and s[i - 1] not in vowel:
        flag = 0
        break
print(flag)