n = int(input())
li_sum = sum(list(map(int, input().split())))

if li_sum > 0:
    print("Right")
elif li_sum == 0:
    print("Stay")
else:
    print("Left")


