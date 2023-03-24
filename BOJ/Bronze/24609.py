n = int(input())

st = 0
res = 0
for _ in range(n):
    num = int(input())

    if st + num < 0:
        res += abs(st + num)
        st = 0
        continue

    st += num

print(res)