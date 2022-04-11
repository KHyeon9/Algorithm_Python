now_hour, now_min, now_second = map(int, input().split(":"))
start_hour, start_min, start_second = map(int, input().split(":"))
result_time = (start_hour - now_hour) * 3600 \
              + (start_min - now_min) * 60 \
              + (start_second - now_second)

if result_time < 0:
    result_time += 3600 * 24

result_hour = result_time // 3600
result_min = result_time % 3600 // 60
result_second = result_time % 60
print("%02d:%02d:%02d"
      % (result_hour, result_min, result_second))
