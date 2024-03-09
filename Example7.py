a = 33
b = 32

# First conditional block
if b > a:
    print("b is greater than a")
# Otherwise if a equals b
elif a == b:
    print("a and b are equal")
# This condition is entered if all previous blocks are not selected.
else:
    print("* Program output *")
    print("b is less than a")

# Second conditional block
if not a == b:
    print("b and a are not equal")