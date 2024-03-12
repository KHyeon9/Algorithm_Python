n = int(input())
waiting = input()
waiting_now = [0] * 10

for w in waiting:
    if w == "L":
        for i in range(10):
            if waiting_now[i] == 0:
                waiting_now[i] = 1
                break
    elif w == "R":
        for i in range(10):
            if waiting_now[9 - i] == 0:
                waiting_now[9 - i] = 1
                break
    else:
        waiting_now[int(w)] = 0

print(*waiting_now, sep="")

