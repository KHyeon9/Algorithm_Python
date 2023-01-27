heart = [" @@@   @@@ ",
         "@   @ @   @",
         "@    @    @",
         "@         @",
         " @       @ ",
         "  @     @  ",
         "   @   @   ",
         "    @ @    ",
         "     @     "]

n = int(input())
for line in heart:
    for i in range(n):
        if i != n - 1:
            print(line, end=" ")
            continue
        print(line, end="")
    print()