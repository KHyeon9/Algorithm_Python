a_list = sorted([int(input()) for _ in range(4)])
b = int(input())

if len(set(a_list)) == 1:
    print(1)

elif a_list[0] + b == a_list[1] and a_list[1] == a_list[2] and a_list[2] == a_list[3]:
    print(1)

else:
    print(0)