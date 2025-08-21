n, m = map(int, input().split())
res = 0

for _ in range(n):
    # 알파벳 범위 지정
    alpa_cnt = [1] * m
    line = input()
    flag = False

    for ch in line:
        i = ord(ch) - 65
        # 범위를 초과하거나 해당 알파벳이 중복 사용된 경우
        if m <= i or alpa_cnt[i] == 0:
            flag = True
            break
        alpa_cnt[i] -= 1
    if flag:
        continue
    # 조건에 해당하지 않으면 +1
    res += 1
print(res)
