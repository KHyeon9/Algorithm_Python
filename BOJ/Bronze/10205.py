for i in range(int(input())):
    head = int(input())
    c_b = input()
    for m in c_b:
        if m == 'c':
            head += 1
        else:
            head -= 1
    print(f"Data Set {i + 1}:")
    print(head)
    print()