h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
time1 = h1 * 3600 + m1 * 60 + s1
time2 = h2 * 3600 + m2 * 60 + s2

time2 += 3600 * 24
res_time = time2 - time1
res_time %= 3600 * 24
if res_time == 0:
    res_time = 3600 * 24

res_h = res_time // 3600
res_m = res_time % 3600 // 60
res_s = res_time % 60

print("%02d:%02d:%02d" % (res_h, res_m, res_s))
