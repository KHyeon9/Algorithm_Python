change = {"e": "i", "i": "e", "E": "I", "I": "E"}
while 1:
    try:
        s = input()
        result = ""
        for i in s:
            if i in change:
                result += change[i]
                continue
            result += i
        print(result)
    except EOFError:
        break
