r, n = map(int, input().split())
# 총 인원
total = [i for i in range(1, r + 1)]
# 돌아온 사람들
returner = list(map(int, input().split()))
# 복귀자 제거
for el in returner:
    total.remove(el)
print(*total if len(total) > 0 else "*")