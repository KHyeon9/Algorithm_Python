from collections import Counter

s = input()
s_cnt = Counter(s)
# 홀수 총 빈도
odd_cnt = sum(1 for v in s_cnt.values() if v % 2 == 1)
# 홀수 계수에 따른 제거 갯수
res = max(0, odd_cnt - 1)

print(res)