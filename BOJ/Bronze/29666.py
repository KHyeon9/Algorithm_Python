ok = ["123", "456", "789", "147", "258", "369", "058"]
s = "".join(sorted(input()))

print("Unlocked" if s in ok else "Locked")
