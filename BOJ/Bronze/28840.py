time1 = list(map(int, input().split(":")))
time2 = list(map(int, input().split(":")))

time1 = time1[0] * 60 + time1[1]
time2 = time2[0] * 60 + time2[1]

time2 += 24 * 60

res = time2 - time1
print(f"{str(res // 60).zfill(2)}:{str(res % 60).zfill(2)}")