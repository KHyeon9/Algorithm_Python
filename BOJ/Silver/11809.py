def solution(string):
    return int(string) if string != '' else "YODA"

n1 = list(input().strip())
n2 = list(input().strip())

for i in range(min(len(n1), len(n2))):
    p = -i -1
    if int(n1[p]) > int(n2[p]):
        n2[p] = ''
    elif int(n1[p]) < int(n2[p]):
        n1[p] = ''

print(solution(''.join(n1)))
print(solution(''.join(n2)))
