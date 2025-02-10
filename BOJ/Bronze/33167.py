def solution(a, b):
    if a == b:
        return 0
    elif (
            (a == "R" and b == "S") or
            (a == "S" and b == "P") or
            (a == "P" and b == "R")
    ):
        return 1
    return -1

n = int(input())
ao = input()
bt = input()
ao_p, bt_p = 0, 0

for i in range(n):
    if solution(ao[i], bt[i]) == 1:
        ao_p += 1
    elif solution(ao[i], bt[i]) == -1:
        bt_p += 1

print(ao_p, bt_p)