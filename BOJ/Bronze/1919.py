s1 = input()
s2 = input()
result = len(s1) + len(s2)
for word in set(s1):
    if word in s2:
        result -= min(s1.count(word), s2.count(word)) * 2
print(result)