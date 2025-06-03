for _ in range(int(input())):
    n, m, l = map(int, input().split())
    s_list = list(map(int, input().split()))
    # 최소 시간 셋팅
    min_time = m - l

    # -1인 경우와  시험 시간을 초과하는 경우 제외
    s_list = [el for el in s_list if 0 <= el <= m]

    # 최소 시간 구하기
    if s_list:
        min_time = min(min_time, min(s_list))
        
    res = m - min_time
    # 1분일 경우 단어 수정
    unit = "minutes" if res != 1 else "minute"
    print(f"The scoreboard has been frozen with {res} {unit} remaining.")