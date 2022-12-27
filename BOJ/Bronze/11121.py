def sol(code1, code2):
    for i in range(len(code1)):
        if code1[i] != code2[i]:
            return False
    return True

for _ in range(int(input())):
    c1, c2 = input().split()
    if sol(c1, c2):
        print("OK")
    else:
        print("ERROR")