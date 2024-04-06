arr = []
for _ in range(3):
    h_s, m_s, h_e, m_e = map(int, input().split())
    time = (h_e * 60 + m_e) - (h_s * 60 + m_s)

    if time < 0:
        time += 60 * 24

    arr.append(time)

min_time = min(arr)
max_time = max(arr)

print(f"{min_time // 60}:{min_time % 60:02}")
print(f"{max_time // 60}:{max_time % 60:02}")
