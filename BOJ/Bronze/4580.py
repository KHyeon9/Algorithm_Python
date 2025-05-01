while True:
    line = list(map(int, input().split()))
    # 0만 입력시 종료
    if line[0] == 0:
        break
    # 사용 갯수
    n = line[0]
    # 사용할 리스트
    li = line[1:]
    # 결과
    res = []
    # 현재 값
    now = 1
    # 리스트 원소에 맞는 갯수 만큼 값 삽입
    for el in li:
        for _ in range(el - len(res)):
            res.append(now)
        now += 1

    print(*res)