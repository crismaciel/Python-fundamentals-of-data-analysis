numDays  = 7
numWeeks = 4

for week in range(1, numWeeks + 1):

    # end="" avoids pointer going to new line.
    print("week " + str(week) + ": ", end="")

    # Show days of week
    for day in range(1, numDays + 1):
        if day==1:
            print("Sunday" + str(day) + "   ", end="")
        elif day==2:
            print("Monday" + str(day) + "   ", end="")
        elif day == 3:
            print("Tuesday" + str(day) + "   ", end="")
        elif day == 4:
            print("Wednesday" + str(day) + "   ", end="")
        elif day == 5:
            print("Thursday" + str(day) + "   ", end="")
        elif day == 6:
            print("Friday" + str(day) + "   ", end="")
        else:
            print("Saturday" + str(day) + "   ", end="")
    print("") # Goes to new line