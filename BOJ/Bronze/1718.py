s = input()
password = input()
while len(password) < len(s):
    password += password
for i in range(len(s)):
    if s[i] == ' ':
        print(' ', end="")
        continue
    trans = ord(s[i]) - ord(password[i]) + ord('a') - 1
    if trans < ord('a'):
        trans += 26
    if trans > ord('z'):
        trans -= 26

    print(chr(trans), end="")
