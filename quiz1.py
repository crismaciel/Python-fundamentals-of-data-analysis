def showReadingGlassesOrder(firstName, lastName, Address, Country, Lenses, Boolean):
    print("********************************************** ")
    if firstName=="Akshay" and Country=="Canada":
        print(firstName + " " + lastName)
        print(Address + ", " + Country)
        print("---------------------------------------------- ")
        if Boolean == True:
            print("Lenses:", Lenses, "x" "(Blue light protection included)")
        else:
            print("Lenses:", Lenses, "x")
        print("Shipping charges are $25.00.")

    if firstName=="Merella" and Country=="Canada":
        print(firstName + " " + lastName)
        print(Address + ", " + Country)
        print("---------------------------------------------- ")
        if Boolean == True:
            print("Lenses:", Lenses, "x" "(Blue light protection included)")
        else:
            print("Lenses:", Lenses, "x")
        print("Shipping charges are $25.00.")

    if firstName=="Rachel" and Country=="US":
        print(firstName + " " + lastName)
        print(Address + ", " + Country)
        print("---------------------------------------------- ")
        if Boolean == True:
            print("Lenses:", Lenses, "x" "(Blue light protection included)")
        else:
            print("Lenses:", Lenses, "x")
        print("Shipping charges are $15.00.")

    if firstName=="Maria" and Country=="Mexico":
        print(firstName + " " + lastName)
        print(Address + ", " + Country)
        print("---------------------------------------------- ")
        if Boolean == True:
            print("Lenses:", Lenses, "x" "(Blue light protection included)")
        else:
            print("Lenses:", Lenses, "x")
        print("Shipping charges are $26.50.")
showReadingGlassesOrder("Akshay", "Tandon","12 Peaceful Place", "Canada", 1.25, False)
showReadingGlassesOrder("Merella", "Fernandez","126 Main Street", "Canada", 1.35, True)
showReadingGlassesOrder("Rachel", "Nichols","18 Sunset Blvd", "US", 1.05, True)
showReadingGlassesOrder("Maria", "Dulce","Paseo de la Reforma", "Mexico", 1.30, False)