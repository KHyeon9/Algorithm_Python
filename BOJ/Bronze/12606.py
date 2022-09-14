for i in range(int(input())):
    line = list(input().split())[::-1]
    print(f"Case #{i + 1}:", end=' ')
    print(*line)