N, m, M, T, R = map(int, input().split())
running, time = 0, 0
heartbeat = m
if m + T > M:
    print(-1)
else:
    while running != N:
        if M >= heartbeat + T:
            heartbeat += T
            running += 1
            time += 1

        else:
            heartbeat -= R
            if heartbeat < m:
                heartbeat = m
            time += 1


    print(time)