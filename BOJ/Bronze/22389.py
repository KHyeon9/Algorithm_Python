while True:
    n, l, r = map(int, input().split())

    # 탈출 조건
    if n == l == r:
        break

    a_list = [int(input()) for _ in range(n)]
    res = 0

    for year in range(l, r + 1):
        flag = False
        for i in range(n):
            # 원소들을 돌면서 배수일 경우
            if year % a_list[i] == 0:
                flag = True
                # 원소의 인덱스가 홀수일 경우 윤년
                if (i + 1) % 2 == 1:
                    res += 1
                break
        # 원소들의 배수가 아닐때 총 원소의 수가 짝수일 경우 윤년
        if not flag and n % 2 == 0:
            res += 1
    print(res)