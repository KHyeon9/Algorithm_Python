l = int(input())
t = int(input())
i = 1
while 1:
    if t * i > l:
        print((t * i) - l)
        break
    i += 1
