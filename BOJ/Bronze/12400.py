ans = "yhesocvxduiglbkrztnwjpfmaq"

for i in range(int(input())):
    s = input()
    print(f"Case #{i + 1}: ", end='')
    for w in s:
        if w.isalpha():
            print(ans[ord(w) - ord('a')], end='')
        else:
            print(w, end='')
    print()
