n = int(input())
t_cnt, s_cnt = 0, 0

for _ in range(n):
    line = input().lower()
    t_cnt += line.count('t')
    s_cnt += line.count('s')

print("English" if t_cnt > s_cnt else "French")

