n = int(input())
str_n = str(n)

if '7' not in str_n and n % 7 != 0:
    print(0)
elif '7' not in str_n and n % 7 == 0:
    print(1)
elif '7' in str_n and n % 7 != 0:
    print(2)
else:
    print(3)