DoW = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
       "Monday", "Tuesday"]
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30,
         31, 30, 31]

d, m = map(int, input().split())

idx = sum(month[:m]) + d - 1

print(DoW[idx % 7])