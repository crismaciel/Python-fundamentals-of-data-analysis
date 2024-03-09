numDays  = 7
numWeeks = 4

for week in range(1, numWeeks + 1):

    # end="" avoids pointer going to new line.
    print("week " + str(week) + ": ", end="")

    # Show days of week
    for day in range(1, numDays + 1):
      print("day" + str(day) + "   ", end="")

    print("") # Goes to new line