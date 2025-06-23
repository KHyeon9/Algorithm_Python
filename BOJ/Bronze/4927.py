def nums_sum(nums):
    return sum(int(num) for num in nums)

t = 0
while True:
    line = input()

    if line == ".":
        break

    t += 1
    line = line[:-1]

    if "*" in line:
        a_str, temp = line.split("*")
        cal = "*"
    else:
        a_str, temp = line.split("+")
        cal = "+"
    b_str, c_str = temp.split("=")

    a = nums_sum(a_str) % 9
    b = nums_sum(b_str) % 9
    c = nums_sum(c_str) % 9

    if cal == "*":
        ab = (a * b) % 9
    else:
        ab = (a + b) % 9

    res = "PASS" if ab == c else "NOT!"
    print(f"{t}. {res}")

