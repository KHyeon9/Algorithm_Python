from datetime import datetime

input_date = datetime.strptime(input(),  "%Y-%m-%d")
target_date = datetime.strptime("2023-10-21",  "%Y-%m-%d")
diff_date = target_date - input_date

if int(diff_date.days) >= 35:
    print("GOOD")
else:
    print("TOO LATE")