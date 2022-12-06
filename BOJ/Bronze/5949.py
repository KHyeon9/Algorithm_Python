num = input()[::-1]
result = ""
for i in range(len(num)):
    result += num[i]
    if (i + 1) % 3 == 0 and i != len(num) - 1:
        result += ","
print(result[::-1])