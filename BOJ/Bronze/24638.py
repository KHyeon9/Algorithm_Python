first = list(input().split())
second = list(input().split())

if "BC" in first:
    first_year = int(first[0])
    if "BC" in second:
        second_year = int(second[0])
        res = abs(first_year - second_year)
    else:
        second_year = int(second[1])
        res = first_year + second_year - 1
else:
    first_year = int(first[1])
    if "BC" in second:
        second_year = int(second[0])
        res = first_year + second_year - 1
    else:
        second_year = int(second[1])
        res = abs(first_year - second_year)
print(res)

