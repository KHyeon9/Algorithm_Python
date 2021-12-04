n = int(input())
cnt = n // 14
if n % 14 in [1, 13]:
    print('baby')
elif n % 14 in [0, 2]:
    print('sukhwan')
elif n % 14 == 5:
    print('very')
elif n % 14 == 6:
    print('cute')
elif n % 14 == 9:
    print('in')
elif n % 14 == 10:
    print('bed')
elif n % 14 in [3, 7, 11]:
    if cnt < 3:
        print('turu' + 'ru' * (cnt + 1))
    else:
        print(f'tu+ru*{cnt + 2}')
elif n % 14 in [4, 8, 12]:
    if cnt < 4:
        print('tu' + 'ru' * (cnt + 1))
    else:
        print(f'tu+ru*{cnt + 1}')
