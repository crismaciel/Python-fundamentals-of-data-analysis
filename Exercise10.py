def showLetterGrade(percentage):
    # end="" avoids pointer going to new line.
    print("The grade " + str(percentage) + " is ", end="")
    if percentage >= 90:
        print("A")
    elif percentage >= 80:
        print("B")
    elif percentage >= 70:
        print("C")
    else:
        print("F")

    # if-elif-else series goes here inside the function.

showLetterGrade(95)
showLetterGrade(72)
showLetterGrade(51)