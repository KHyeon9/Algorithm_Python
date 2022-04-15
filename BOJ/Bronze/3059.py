for i in range(int(input())):
    Sum = 2015
    s = set(input())
    for word in s:
        Sum -= ord(word)
    print(Sum)