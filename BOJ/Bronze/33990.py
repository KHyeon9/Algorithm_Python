now, res = 600, -1

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    # 무게의 총합
    sum_kg = a + b + c
    # 512kg 이상인 경우
    if sum_kg >= 512:
        # 무게 차이 계산
        diff = abs(512 - sum_kg)
        # 무게 차이가 현제 값의 무게 차이보다 적은 경우
        if diff < now:
            res = sum_kg
            now = diff
print(res)


