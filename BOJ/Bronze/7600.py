while 1:
    s = input()
    if s == '#':
        break
    arr = [0] * 26
    for w in s:
        w = w.lower()
        if w.isalpha():
            idx = ord(w) - ord('a')
            arr[idx] += 1
    print(26 - arr.count(0))
