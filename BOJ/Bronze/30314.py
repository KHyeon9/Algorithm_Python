n = int(input())
line1 = input()
line2 = input()
res = 0
for i in range(n):
    distance = abs(ord(line1[i]) - ord(line2[i]))
    res += min(distance, 26 - distance)

print(res)