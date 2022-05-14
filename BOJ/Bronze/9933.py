n = int(input())
passwords = [input() for _ in range(n)]
for password in passwords:
    if password[::-1] in passwords:
        print(len(password), password[len(password) // 2])
        break