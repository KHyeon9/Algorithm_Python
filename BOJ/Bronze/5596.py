MG, MG2, MG3, MG4 = list(map(int, input().split()))
MS, MS2, MS3, MS4 = list(map(int, input().split()))

MGS = MG + MG2 + MG3 + MG4
MSS = MS + MS2 + MS3 + MS4

if MGS // 4 >= MSS // 4:
    print(MGS)

else:
    print(MSS)