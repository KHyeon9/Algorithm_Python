n = int(input())
a_list = list(map(int, input().split()))
even = len([el for el in a_list if el % 2 == 0])
odd = n - even

print(even * odd)