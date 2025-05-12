numbers = list(input().split())
num = input()
num_len = len(num)
res = 0

for number in numbers:
    if number != num and number[:num_len] == num:
        res += 1

print(res)
