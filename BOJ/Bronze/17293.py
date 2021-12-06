n = int(input())
for i in range(n, -1, -1):
    if i == 0:
        print('No more bottles of beer on the wall, no more bottles of beer.')
        if n == 1:
            print('Go to the store and buy some more, 1 bottle of beer on the wall.')
        elif n == 0:
            print('Go to the store and buy some more, no more bottles of beer on the wall.')
        else:
            print(f'Go to the store and buy some more, {n} bottles of beer on the wall.')
    elif i == 1:
        print('1 bottle of beer on the wall, 1 bottle of beer.')
        print('Take one down and pass it around, no more bottles of beer on the wall.')
    else:
        print(f'{i} bottles of beer on the wall, {i} bottles of beer.')
        if i == 2:
            print(f'Take one down and pass it around, {i - 1} bottle of beer on the wall.')
        else:
            print(f'Take one down and pass it around, {i - 1} bottles of beer on the wall.')
    print()
