n = int(input())
s = input()
cnt = s.count('L')
print(min(n + 1 - (cnt // 2), n))


