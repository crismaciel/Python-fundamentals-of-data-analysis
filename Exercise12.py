def showBalanceSchedule(firstName, balance, interestRate, yearsRemaining):
    print("* Balance foreacast for " + firstName + "*")
    if interestRate==0:
        print('NA')
    else:
        yearCount=0
        while yearsRemaining -yearCount>0:
            yearCount+=1
            balance = balance*interestRate
            roundedBalance = round(balance,2)
            print("Year" + str(yearCount) + ": " + str(roundedBalance))
showBalanceSchedule("Louise",
                    5.25, 1.07, 7)
showBalanceSchedule("Larry",
                    52.25, 0, 6)
showBalanceSchedule("Mehri",
                    152.25, 1.15, 6)