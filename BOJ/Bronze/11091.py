a = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(int(input())):
    s = input().lower()
    result = ''
    for i in a:
        if i not in s:
            result += i
    if len(result) == 0:
        print('pangram')
    else:
        print(f'missing {result}')
