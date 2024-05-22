import pylab

retry = "y"

while retry =="y":

    # Get the required UserInputs
    print("")
    annual_salary     = float(input("Enter your annual salary: ".ljust(60)))
    portion_saved     = float(input("Enter the percent of your salary to save, as percent: ".ljust(60)))/100
    total_cost        = float(input("Enter the const of your dream home: ".ljust(60)))
    semi_annual_raise = float(input("Enter the semi-annual raise, as percent: ".ljust(60)))/100

    # Calculate monthly_salary
    monthly_salary = annual_salary / 12

    # Calculate the required down_payment
    portion_down_payment = 0.25
    down_payment = total_cost * portion_down_payment


    savingsreturns= 0.04

    #StartVariablesfor Savings and Months
    current_savings = 0.0
    savingsreturnaccumulated = 0.0
    monthlysavingsaccumulated = 0.0
    months = 0

    #PlotData
    savingsaccountbalance = []
    down_payment_cost = []
    savingsreturndata = []
    monthlysavingsdata = []
    portionsaveddata = []
    while current_savings < down_payment:

        
        # increase month counter
        months += 1

        #print(str(months).rjust(4)+":", "SavingsStart:      ", current_savings)

        savings_return = current_savings * savingsreturns / 12
        savingsreturnaccumulated += savings_return
        #print(str(months).rjust(4)+":", "SavingsReturn:     ", savings_return)
        #print(str(months).rjust(4)+":", "AddedToSavings:    ", monthly_salary * portion_saved)

        monthlysavings = monthly_salary * portion_saved
        monthlysavingsaccumulated += monthlysavings
        current_savings = current_savings + savings_return + monthlysavings

        #print(str(months).rjust(4)+":", "SavingsEnd:        ", current_savings)

        # half annual raise 
        if months%6 == 0 and months !=0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)


        # fill PlotData
        savingsaccountbalance.append(current_savings)
        down_payment_cost.append(down_payment)
        savingsreturndata.append(savingsreturnaccumulated)
        monthlysavingsdata.append(monthlysavingsaccumulated)


    print("Number of months:".ljust(59), months)


    #PlotData
    if input("Print Plot? [y]: ".ljust(60)) == "y":
        pylab.plot(savingsaccountbalance, '-g', label='Total Savings')
        pylab.plot(down_payment_cost, '-b', label='Required Down Payment')
        pylab.plot(savingsreturndata, '-c', label='Investment Returns (accumulated)')
        pylab.plot(monthlysavingsdata, '-m', label='Monthly Savings (accumulated)')
        pylab.title('Financial')
        pylab.xlabel('Months')
        pylab.ylabel('Money')
        pylab.legend(loc='upper left')
        pylab.show()
    
    print("")
    retry = input("Retry [y]:".ljust(60))
