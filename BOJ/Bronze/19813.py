for _ in range(int(input())):
    line = input()
    if '.' in line:
        d, m, y = map(int, line.split('.'))
        print(f"{d:02}.{m:02}.{y:04} {m:02}/{d:02}/{y:04}")
    else:
        m, d, y = map(int, line.split('/'))
        print(f"{d:02}.{m:02}.{y:04} {m:02}/{d:02}/{y:04}")
