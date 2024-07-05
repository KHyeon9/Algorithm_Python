def convert(s):
    return int("".join(s.split("."))[1:])

n = int(input())
now = convert(input())
res = 0

for _ in range(n):
    input_money = convert(input())
    now += input_money

    if now % 100:
        res += 1
print(res)