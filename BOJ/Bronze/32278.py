def solution(n):
    if -32768 <= n <= 32767:
        return "short"
    elif -2147483648 <= n <= 2147483647:
        return "int"
    else:
        return "long long"

print(solution(int(input())))