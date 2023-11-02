n = int(input())
x_list = list(map(int, input().split()))
l_list = list(map(int, input().split()))
c_list = list(input().split())

for i in range(n):
    for j in range(i + 1, n):
        if abs(x_list[i] - x_list[j]) <= l_list[i] + l_list[j]:
            if c_list[i] != c_list[j]:
                print("YES")
                print(i + 1, j + 1)
                exit()

print("NO")
