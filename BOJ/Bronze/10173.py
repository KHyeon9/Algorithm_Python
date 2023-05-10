while 1:
    line = input()

    if line == 'EOI':
        break

    print('Found' if 'nemo' in line.lower() else 'Missing')