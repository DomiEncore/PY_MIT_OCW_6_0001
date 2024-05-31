import math


def calcSavingsAfterMonths(months, startMonthlySalary, semiAnnualRaise, portionSaved, savingsReturnRate):
    
    monthly_salary = startMonthlySalary
    savings = 0
    iMonths = 0
    while iMonths < months:
        
        # increase month counter
        iMonths += 1

        savings_return = savings * savingsReturnRate / 12
        monthly_savings = monthly_salary * portionSaved
        savings += savings_return + monthly_savings
        # print("savingsafter".rjust(50), iMonths+1, round(savings,2))
        # half annual raise
        if iMonths%6 == 0:
            monthly_salary = monthly_salary * (1 + semiAnnualRaise)

    # print("")
    return savings



# Get the required UserInputs
annual_salary_string     = input("Enter your annual salary: ".ljust(60))

while annual_salary_string != "":
    annual_salary = float(annual_salary_string)

    # static Inputs
    total_cost        = 1000000
    semi_annual_raise = 0.07
    savings_return_rate= 0.04
    target_months = 36
    portion_down_payment = 0.25

    # Calculate monthly_salary
    monthly_salary = annual_salary / 12

    # Calculate the required down_payment
    down_payment = total_cost * portion_down_payment

    #check if down payment possible
    if calcSavingsAfterMonths(target_months,monthly_salary,semi_annual_raise,1,savings_return_rate) < down_payment:
        print("it Is not possible to pay the down payment in", target_months, "Months")
        print("")

    #get optimal savings rate with bisection search
    else:
        epsilon = 100

        portionsaved_low = 0
        portionsaved_high= 10000


        portionsaved_guess = (portionsaved_low + portionsaved_high) // 2


        num_guesses=1
        # print("NumGuesses:".ljust(59), num_guesses)
        # print("ThisTryPortionSavedGuess:".ljust(59), portionsaved_guess/10000)
        thistrysavings = calcSavingsAfterMonths(target_months,monthly_salary,semi_annual_raise,portionsaved_guess/10000,savings_return_rate)
        # print("ThisTrySavings:".ljust(59),round(thistrysavings,1))
        # print("Offset:".ljust(59), round(thistrysavings - down_payment,1))
        # print("")


        while abs(thistrysavings - down_payment) >= epsilon and num_guesses < 10000:
            if thistrysavings < down_payment:
                portionsaved_low = portionsaved_guess
            else:
                portionsaved_high = portionsaved_guess

            portionsaved_guess = (portionsaved_low + portionsaved_high) // 2
            num_guesses +=1
            # print("NumGuesses:".ljust(59), num_guesses)
            # print("ThisTryPortionSavedGuess:".ljust(59), portionsaved_guess/10000)
            thistrysavings = calcSavingsAfterMonths(target_months,monthly_salary,semi_annual_raise,portionsaved_guess/10000,savings_return_rate)
            # print("ThisTrySavings:".ljust(59),round(thistrysavings,1))
            # print("Offset:".ljust(59), round(thistrysavings - down_payment,1))
            # print("")



        print("Best savings rate:".ljust(59), str(portionsaved_guess/10000*100)+"%")
        print("Number of guesses:".ljust(59), num_guesses)
        print("")

    # Request new Get the required UserInputs
    annual_salary_string     = input("Enter your annual salary: ".ljust(60))