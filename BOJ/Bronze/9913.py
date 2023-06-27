cnt_dict = {}

for _ in range(int(input())):
    n = int(input())

    if n not in cnt_dict:
        cnt_dict[n] = 1
    else:
        cnt_dict[n] += 1

print(max(cnt_dict.values()))