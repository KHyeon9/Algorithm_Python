for i in range(100, 1000):
    for j in range(100, 1000):
        if i % 111 == 0 and j % 111 == 0:
            continue
        if (i * (j % 100) == j * (i // 10)) and (i % 10 == j // 100):
            print(f"{i} / {j} = {i // 10} / {j % 100}")