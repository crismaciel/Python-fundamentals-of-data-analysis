def showMedicalStatus(firstName, age, highBloodPressure):
     if firstName == "Bob" and age == 60:
         print("Medical alert: " + firstName, "see a doctor.")
     elif firstName == "Jane" and age == 60:
         print(firstName, "you are in good health. See you next checkup")
     else:
        print("Warning: " + firstName, "seeing a doctor is recommended.")
showMedicalStatus("Bob", 60, True)
showMedicalStatus("Jane", 60, False)
showMedicalStatus("Brad", 28, True)

