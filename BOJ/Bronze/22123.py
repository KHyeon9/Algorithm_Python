for _ in range(int(input())):
    s, f, m = input().split()

    s_h, s_m, s_s = map(int, s.split(":"))
    f_h, f_m, f_s = map(int, f.split(":"))
    m = int(m) * 60

    s_total = s_h * 3600 + s_m * 60 + s_s
    f_total = f_h * 3600 + f_m * 60 + f_s

    test_time = f_total - s_total

    if test_time <= 0:
        test_time += 86400

    if test_time >= m:
        print("Perfect")
    elif test_time + 3600 >= m:
        print("Test")
    else:
        print("Fail")