p, q = map(int, input().split())
p_list = [i for i in range(1, p + 1) if p % i == 0]
q_list = [i for i in range(1, q + 1) if q % i == 0]

for i in p_list:
    for j in q_list:
        print(i, j)