gan_points = [1, 2, 3, 3, 4, 10]
sa_points = [1, 2, 2, 2, 3, 5, 10]

for tc in range(1, int(input()) + 1):
    human = list(map(int, input().split()))
    monster = list(map(int, input().split()))
    h_point, m_point = 0, 0

    for i in range(6):
        h_point += gan_points[i] * human[i]

    for i in range(7):
        m_point += sa_points[i] * monster[i]

    if h_point > m_point:
        print(f"Battle {tc}: Good triumphs over Evil")

    elif h_point < m_point:
        print(f"Battle {tc}: Evil eradicates all trace of Good")

    else:
        print(f"Battle {tc}: No victor on this battle field")