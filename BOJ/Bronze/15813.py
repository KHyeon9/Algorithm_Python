n = int(input())
name = input()
res = 0

for i in range(n):
    res += ord(name[i]) - ord('A') + 1

print(res)