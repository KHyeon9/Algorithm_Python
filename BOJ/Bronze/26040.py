s = input()
w = list(input().split())
result = ""
for i in s:
    if i in w:
        result += i.lower()
        continue
    result += i
print(result)