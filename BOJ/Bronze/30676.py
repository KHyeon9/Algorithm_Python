def solution(num):
    if 620 <= num <= 780:
        return "Red"
    elif 590 <= num < 620:
        return "Orange"
    elif 570 <= num < 590:
        return "Yellow"
    elif 495 <= num < 570:
        return "Green"
    elif 450 <= num < 495:
        return "Blue"
    elif 425 <= num < 450:
        return "Indigo"
    elif 380 <= num < 425:
        return "Violet"

print(solution(int(input())))