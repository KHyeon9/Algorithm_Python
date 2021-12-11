t = int(input())
q = [0, 0, 0, 0, 0]

for i in range(t):
    x, y = list(map(int, input().split()))

    if x > 0 and y > 0:
        q[0] += 1

    elif x < 0 and y > 0:
        q[1] += 1

    elif x < 0 and y < 0:
        q[2] += 1

    elif x > 0 and y < 0:
        q[3] += 1

    else:
        q[4] += 1

print("Q1: %d" % q[0])
print("Q2: %d" % q[1])
print("Q3: %d" % q[2])
print("Q4: %d" % q[3])
print("AXIS: %d" % q[4])