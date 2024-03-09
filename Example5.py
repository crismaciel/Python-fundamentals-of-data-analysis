# This function receives a first and last name as parameters and displays
# it as formatted output.
def showFullName(firstName, middleName, lastName):
    # Python requires that all code belonging to the function be indented.
    output = "* Full Name: " + firstName + " " + middleName + " " + lastName + " *"
    print(output)

a = input("Your first name: ")
b = input("Your middle name: ")
c = input("Your last name: ")
# These instructions call our functions.
showFullName("Jane", "Jenny", "Jones")
print(" Your full name is: " , a, b, c)
