start_h, start_m, start_s = map(int, input().split(":"))
end_h, end_m, end_s = map(int, input().split(":"))
# 12시를 지나는 횟수 계산
res_hour = 1 if start_h < 12 <= end_h else 0
res_min = end_h - start_h
res_sec = (end_h - start_h) * 60 + (end_m - start_m)

print(f"{res_hour} {res_min} {res_sec}")
