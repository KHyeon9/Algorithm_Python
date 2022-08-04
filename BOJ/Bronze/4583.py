mirror = ['b', 'd', 'p', 'q', 'i', 'o', 'v', 'w', 'x']
dic = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}
while 1:
    s = input()
    result = ""

    if s == '#':
        break

    for i in s:
        if i not in mirror:
            result = "INVALID"[::-1]
            break
        if i in dic:
            result += dic[i]
        else:
            result += i
    print(result[::-1])
