for _ in range(int(input())):
    alpha_cnt = [0] * 26
    s = input()
    for i in s:
        if i == ' ':
            continue
        alpha_cnt[ord(i) - 97] += 1
        max_cnt = max(alpha_cnt)
    print(chr(alpha_cnt.index(max_cnt) + 97) if alpha_cnt.count(max_cnt) < 2 else '?')
