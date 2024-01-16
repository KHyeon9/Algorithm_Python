n = int(input())
k = int(input())
s = input()
r_cnt = s.count('R')

print("R" if r_cnt < k else "W")
