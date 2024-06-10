n = int(input())
cnts, sums = [0] * 46, [0] * 46

for _ in range(n):
    s = input()

    for i in range(len(s)):
        sums[i] += ord(s[i])
        cnts[i] += 1

res = ""

for i in range(46):
    if cnts[i] == 0:
        break
    res += chr(sums[i] // cnts[i])

print(res)