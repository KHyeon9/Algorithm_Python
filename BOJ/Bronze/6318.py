t = 0
while True:
    n = int(input())
    # 탈출 조건
    if n == 0:
        break
    # 반복 횟수
    t += 1
    nums = list(map(int, input().split()))
    # 평균값 구하기
    avg = sum(nums) // n
    res = 0

    for num in nums:
        res += num - avg if num > avg else 0

    print(f"Set #{t}")
    print(f"The minimum number of moves is {res}.\n")

