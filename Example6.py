def fehrenheit(t):
   celsius = (t * 1.8) + 32
   return celsius # This return statement exits the function and gives a value
                  # to the calling instruction.

t = float(input("Enter with the temperature in celsius: ")) # This is the calling instruction.
result = fehrenheit(t)
print("The temperature in fehrenheit is ", + result)


