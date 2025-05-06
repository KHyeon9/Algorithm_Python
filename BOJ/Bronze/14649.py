p = int(input())
# 색칠할 배열 생성
arr = [0] * 101

for _ in range(int(input())):
    num, direction = input().split()
    num = int(num) # 정수로 변경

    # 방향에 따른 색칠
    if direction == "R":
        for i in range(num + 1, 101):
            arr[i] += 1
    else:
        for i in range(1, num):
            arr[i] += 1

# 색칠값 갯수를 저장할 배열 생성
res = [0, 0, 0]

# 색칠된 갯수에 따른 분배
for i in range(1, 101):
    color = arr[i] % 3
    res[color] += 1

# 결과 출력
for el in res:
    print(f"{p * (el / 100):.2f}")