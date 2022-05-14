zero = ["***", "* *", "* *", "* *", "***"]
one = ["  *", "  *", "  *", "  *", "  *"]
two = ["***", "  *", "***", "*  ", "***"]
three = ["***", "  *", "***", "  *", "***"]
four = ["* *", "* *", "***", "  *", "  *"]
five = ["***", "*  ", "***", "  *", "***"]
six = ["***", "*  ", "***", "* *", "***"]
seven = ["***", "  *", "  *", "  *", "  *"]
eight = ["***", "* *", "***", "* *", "***"]
nine = ["***", "* *", "***", "  *", "***"]
one2 = ["*", "*", "*", "*", "*"]

nums = [zero, one, two, three, four, five, six, seven, eight, nine]
boom = [input() for _ in range(5)]
result = ""
for i in range(0, len(boom[0]), 4):
    num = []
    for j in range(5):
        num.append(boom[j][i:i + 3])
    for j in range(10):
        if num == one2:
            result += '1'
            break
        if num == nums[j]:
            result += str(j)
            break
print("BEER!!" if int(result) % 6 == 0 else "BOOM!!")
