alpa = input()
yonsei = "ILOVEYONSEI"
result = 0

for w in yonsei:
    result += abs(ord(w) - ord(alpa))
    alpa = w
print(result)