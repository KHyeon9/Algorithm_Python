# 월 계산
month_dict = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

while True:
    day, month = input().split()
    # 탈출 조건
    if day == "0" and month == "#":
        break

    month = month_dict[month]
    day = int(day)
    # 없는 생일
    if month == 2 and day == 29:
        print("Unlucky")
    # 같은 날인 경우
    elif month == 8 and day == 4:
        print("Happy birthday")
    else:
        # 8/4 보다 큰 경우
        if month > 8 or (month == 8 and day > 4):
            print("No")
        # 8/4 보다 작은 경우
        else:
            print("Yes")