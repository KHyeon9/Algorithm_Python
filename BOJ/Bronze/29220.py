flag = False

k = int(input())
n = int(input())

a_list = list(map(int, input().split()))
a_sum = sum(a_list)

for a in a_list:
    if a_sum - a >= k:
        flag = True
        break

print("YES" if flag else "NO")