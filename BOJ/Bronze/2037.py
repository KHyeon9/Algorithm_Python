nums = [[], [], ['A', 'B', 'C'], ['D', 'E', 'F'],
        ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],
        ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'],
        ['W', 'X', 'Y', 'Z'], []]

p, w = map(int, input().split())
s = input()
time = 0
now = -1
for word in s:
    if word == ' ':
        time += p
        now = ' '
    else:
        for i in range(10):
            if word in nums[i]:
                if now == i:
                    time += w
                time += (nums[i].index(word) + 1) * p
                now = i
print(time)