def Scholarship(list) :
    avg = sum(list) / len(list)

    if avg == 5:
        return "Named"
    if avg >= 4.5 and 3 not in list:
        return "High"
    if 3 in list:
        return "None"
    return "Common"



scores = [int(input()) for _ in range(int(input()))]

print(Scholarship(scores))