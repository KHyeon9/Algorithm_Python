n = int(input())
x = int(''.join(list(input().split())))
y = int(''.join(list(input().split())))

print(x if x < y else y)