for _ in range(int(input())):
    n, m = input().split()
    a = int(n, 2)
    b = int(m, 2)
    and_answer = bin(a & b)[2:]
    n_cnt = n.count('1')
    m_cnt = m.count('1')
    answer_cnt = and_answer.count('1')
    print(max(n_cnt - answer_cnt, m_cnt - answer_cnt))

