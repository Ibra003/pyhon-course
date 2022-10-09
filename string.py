from unicodedata import name


# break print two line
print("ibrahim\ndeveloper")

print("welcome\"magogoni")

# upper or lower
name="cash money"
print(name + "is developer")
print(name.isupper())

print(name.upper().isupper())
# check the length 
print(len(name))

# print with what you want in string
print(name[0])
print(name[-1])

print(name.index("m"))

# replace function
print(name.replace("cash", "hero"))