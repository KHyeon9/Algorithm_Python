for i in range(3):
    H, M, S, H2, M2, S2 = list(map(int, input().split()))

    HR = H2 - H
    MR = M2 - M
    SR = S2 - S

    if MR < 0:
        HR -= 1
        MR += 60

    if SR < 0:
        if MR > 0:
            MR -= 1
            SR += 60

        elif MR == 0:
            HR -= 1
            MR = 59
            SR += 60

    print(HR, MR, SR)
