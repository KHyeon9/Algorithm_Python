s = list(input().split())
check = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
s2 = s[1:]
print(s[0][0].upper(), end='')
for i in s2:
    if i not in check:
        print(i[0].upper(), end='')