n = int(input())
res = ""

for word in input():
    if word == "I":
        res += "i"
    else:
        res += "L"

print(res)