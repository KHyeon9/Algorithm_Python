H, M, S = map(int, input().split(':'))
H2, M2, S2 = map(int, input().split(':'))

hr = H2 - H
mr = M2 - M
sr = S2 - S

if sr < 0:
    sr += 60
    mr -= 1

if mr < 0:
    mr += 60
    hr -= 1

if hr < 0:
    hr += 24

print((hr * 3600) + (mr * 60) + sr)