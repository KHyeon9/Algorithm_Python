res = 0
hay_bales = [int(input()) for _ in range(int(input()))]
avr = sum(hay_bales) // len(hay_bales)

for i in hay_bales:
    if avr < i:
        res += i - avr
print(res)