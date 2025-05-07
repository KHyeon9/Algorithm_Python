A, a, B, b, P = map(int, input().split())

# 맨 밖 원의 크기보다 크면 No
if A > P or B > P:
    print("No")
# 2개 내부 원의 지름의 합이 맨 밖의 원보다 작으면 Yes
elif A + B <= P:
    print("Yes")
# 내부 원이 밖의 원보다 작으면 Yes
elif a >= B or A <= b:
    print("Yes")
else:
    print("No")
