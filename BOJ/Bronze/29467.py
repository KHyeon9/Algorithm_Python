s = input()

s_list = set()

for i in range(len(s)):
    for j in range(i, len(s) + 1):
        s_list.add(s[i:j])

print(sorted(s_list)[-1])
