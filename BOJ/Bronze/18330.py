n = int(input())
k = int(input())

s = 60 + k

if n < s:
    print(1500 * n)

else:
    print(1500 * s + 3000 * (n-s))