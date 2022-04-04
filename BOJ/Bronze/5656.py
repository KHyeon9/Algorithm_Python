i = 1
while 1:
    li = input()
    if li[2] == 'E':
        break
    else:
        print(f"Case {i}: {str(eval(li)).lower()}")
    i += 1
