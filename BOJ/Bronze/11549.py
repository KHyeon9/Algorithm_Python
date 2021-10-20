tn = int(input())
t_list = list(map(int, input().split()))
cnt = 0

for i in range(5):
    if tn == t_list[i]:
        cnt += 1

print(cnt)