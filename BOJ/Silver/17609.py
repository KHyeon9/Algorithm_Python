for _ in range(int(input())):
    s = input()
    start, end = 0, len(s) - 1
    if s == s[::-1]:
        print(0)
    else:
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                if s[start:end] == s[start:end][::-1] or s[start + 1:end + 1] == s[start + 1:end + 1][::-1]:
                    cnt = 1
                    break
                else:
                    cnt = 2
                    break
        print(cnt)