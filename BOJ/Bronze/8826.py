for _ in range(int(input())):
    n = input()
    direction = input()
    print(
        abs(direction.count('W') - direction.count('E')) +
        abs(direction.count('N') - direction.count('S'))
    )