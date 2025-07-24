s = input()

# 2보다 작은 경우
if len(s) <= 2:
    print(len(s))
else:
    res = 0
    cnts = [0] * 26
    # 각 단어마다 빈도수 계산
    for el in s:
        cnts[ord(el) - ord('a')] += 1
    # 오름차순 정렬
    cnts.sort()
    # 빈도수가 가장 작은 순으로 2단어 남을때 까지 제거
    for cnt in cnts[:-2]:
        res += cnt
    print(res)