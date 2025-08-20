n = int(input())
# a가 2개 이상인데 b로 끝나지 않는 경우 막기위해 b 더하기
line = input() + 'b'
res = 0
now = 0

for el in line:
    # a인 경우 현재까지 a의 개수에 +1
    if el == 'a':
        now += 1
    else:
        # b이고 a의 객수가 1개 초과인 경우
        if now > 1:
            res += now
        # 현제 a 갯수 초기화
        now = 0
print(res + now)
