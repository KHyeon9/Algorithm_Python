for _ in range(int(input())):
    s = input()
    a_cnt = s.count('a')
    b_cnt = s.count('b')

    print(min(a_cnt, b_cnt))