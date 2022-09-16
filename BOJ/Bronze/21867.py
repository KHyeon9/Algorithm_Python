n = int(input())
s = input()
res = ""

for i in s:
    if i in ['J', 'A', 'V']:
        continue
    res += i
print(res if res else "nojava")
