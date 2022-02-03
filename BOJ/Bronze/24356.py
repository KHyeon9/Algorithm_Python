t1, m1, t2, m2 = map(int, input().split())
time = t1 * 60 + m1
time2 = t2 * 60 + m2
result = time2 - time
if result < 0:
    result += 1440
print(result, result // 30)