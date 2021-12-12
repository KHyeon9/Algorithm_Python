x = list(map(int, input().split()))
y = list(map(int, input().split()))
r = 0

for i in range(5):
    if x[i] != y[i]:
        r += 1
if r == 5:
    print("Y")
else:
    print("N")