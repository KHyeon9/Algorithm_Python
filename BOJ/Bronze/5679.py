while True:
    n = int(input())
    # 탈출 조건
    if n == 0:
        break
    max_val = n
    temp = n
    # 1이 나올때 까지 검사
    while temp != 1:
        # 짝수인 경우
        if temp % 2 == 0:
            temp //= 2
        # 홀수인 경우
        else:
            temp = temp * 3 + 1
        max_val = max(max_val, temp)
    print(max_val)
