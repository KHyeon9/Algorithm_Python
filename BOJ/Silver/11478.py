s = input()
arr = []
for i in range(len(s)):
    for j in range(i, len(s)):
        words = s[i:j + 1]
        arr.append(words)
print(len(set(arr)))
