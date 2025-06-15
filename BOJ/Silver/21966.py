n = int(input())
s = input()

if n < 26:
    print(s)
else:
    middle = s[11:-11]
    if "." in middle and "." in middle[:-1]:
        print(s[:9] + "......" + s[-10:])
    else:
        print(s[:11] + "..." + s[-11:])

