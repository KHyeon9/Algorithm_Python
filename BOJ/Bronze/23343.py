n = list(input().split())
if len(n) == 1:
    print('NaN')
elif n[0].isdigit() and n[1].isdigit():
    print(int(n[0]) - int(n[1]))
else:
    print('NaN')