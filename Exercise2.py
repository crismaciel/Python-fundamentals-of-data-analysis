def showFruitList(fruitList):
    print("\n*** DISPLAYING ARRAY CONTENTS")

    # Loop from 0 to 1 - length of array.
    for i in range(len(fruitList)):
        print(fruitList[i])


# Create array.
fruit = ["apples"]

# Add items to array.
fruit.append("pears")
fruit.insert(0, "plums")

# Show array contents.
showFruitList(fruit)

# Remove third element (counting starts at 0).
fruit.pop(2)

# Show array contents.
showFruitList(fruit)