islands = ["Hawaii", "Maui", "Oahu"]

print("The array length is " + str(len(islands))  + ".")

for index in range(0, len(islands)):
    print("index " + str(index) + ": " + islands[index])

print("\nHere is the list again.\n")

for island in islands:
    print(island)
