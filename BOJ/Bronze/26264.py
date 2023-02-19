n = int(input())
s = input()
bd = s.count("bigdata")
sc = s.count("security")
if bd > sc:
    print("bigdata?")
elif bd < sc:
    print("security!")
else:
    print("bigdata? security!")
