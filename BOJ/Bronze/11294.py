import string

def solution(n, f):
    res = ""
    temp = string.digits + string.ascii_uppercase
    while n > 0:
        n, mod = n // f, n % f
        res += temp[mod]

    return res[::-1]

while True:
    name = input()

    if name == "#":
        break

    formation = int(input())
    num = int(input())

    print(f"{name}, {num}, {solution(num, formation)}")