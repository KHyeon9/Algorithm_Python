n = int(input())
cnt, total = 0, 0
start, end = 0, 0
while n >= end >= start:
    if total == n:
        cnt += 1
        end += 1
        total = total - start + end
        start += 1
    elif total > n:
        total -= start
        start += 1
    else:
        end += 1
        total += end

print(cnt)