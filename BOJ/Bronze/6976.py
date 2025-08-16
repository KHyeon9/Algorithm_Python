for _ in range(int(input())):
    num = int(input())
    # 처음 숫자 저장
    start_num = num
    # 100보다 클때 진행
    while num >= 100:
        print(num)
        # 10으로 나누고 10으로 나눈 나머지를 뺌
        num = num // 10 - num % 10
    print(num)
    # 첫 숫자가 11로 나눴을 때, 0인지 확인
    if start_num % 11 == 0:
        print(f"The number {start_num} is divisible by 11.")
    else:
        print(f"The number {start_num} is not divisible by 11.")
    print()