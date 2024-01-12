n, m = map(int, input().split())
s_list = list(input().split())
t_list = list(input().split())

for _ in range(int(input())):
    year = int(input())
    res = s_list[year % n - 1] + t_list[year % m - 1]
    print(res)