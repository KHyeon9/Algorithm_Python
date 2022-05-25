n = int(input())
s = bin(n + 1)[3:]
print(s.replace('0', '4').replace('1', '7'))