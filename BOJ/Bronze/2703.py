for _ in range(int(input())):
    s = input()
    arr = input()
    result = ''
    for word in s:
        if word == ' ':
            result += ' '
        else:
            result += arr[ord(word) - 65]
    print(result)
