while 1:
    try:
        n = int(input())
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        one_to_zero = []
        res = 1
        while 1:
            num = n * res
            for i in str(num):
                i = int(i)
                if i not in one_to_zero:
                    one_to_zero.append(i)
            one_to_zero.sort()
            if one_to_zero == nums:
                print(res)
                break
            res += 1

    except EOFError:
        break