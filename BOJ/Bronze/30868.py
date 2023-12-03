for _ in range(int(input())):
    n = int(input())
    plus = n // 5
    stick = n % 5

    print("++++ " * plus + "|" * stick)