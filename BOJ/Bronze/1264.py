arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while 1:
    s = input()
    if s == '#':
        break
    r = 0
    for i in arr:
        r += s.count(i)
    print(r)
