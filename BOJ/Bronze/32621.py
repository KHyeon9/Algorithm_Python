def solution(line):
    li = line.split("+")
    if len(li) != 2 or li[0] != li[1]:
        return False
    if not li[0].isdigit() or not li[1].isdigit():
        return False
    if li[0] == "0" or li[1] == "0":
        return False
    return True
input_val = input()

print("CUTE" if solution(input_val) else "No Money")



