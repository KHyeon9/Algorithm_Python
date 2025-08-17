n, p = map(int, input().split())
num_str = str(n ** p)
# 70자씩 출력
for i in range(len(num_str) // 70):
    print(num_str[70 * i:70 * (i + 1)])
# 남은 숫자가 있는 경우 출력
remain = len(num_str) % 70
if remain > 0:
    print(num_str[len(num_str) - remain:])