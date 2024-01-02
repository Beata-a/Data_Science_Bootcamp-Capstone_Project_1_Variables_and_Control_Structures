# Importing math package
import math
# Asking the user for input based on selection. The input is not case sensitive as it will be cast to lowercase.
user_input = input("\nInvestment - To calculate the amount of interest you'll earn on your investment. \n \n Bond - To calculate the amount you'll have to pay on a home loan. \n \nPlease enter either 'investment' or 'bond' from the menu above to proceed: ")
user_input_lower = user_input.lower()
# Creating a while loop condition where if the user input is not either bond or investment it will loop through repeatedly until one of the two keywords are input
while user_input_lower != "bond" and user_input_lower != "investment":
    print("\n \nThis is not one of permitted options. \nPlease try again")
    user_input = input("\n Investment - To calculate the amount of interest you'll earn on your investment. \n \nBond - To calculate the amount you'll have to pay on a home loan. \n \nPlease enter either 'investment' or 'bond' from the menu above to proceed: ")
    user_input_lower = user_input.lower()
# If the user enters the word bond. Will ask about house value, interest rate and the amount of months they want to take the bond for. Using input to calculate the bond repayment formula. Printing the answer to user.
if user_input_lower == "bond":
    house_value = int(input("\nPlease enter the current value of the house: "))
    interest = float(input("\nPlease enter the interest rate: "))
    interest_yearly = interest/100
    interest_rate_monthly = interest_yearly/12
    repayment_rate = int(input("\nPlease enter the amount of months that you plan to take to repay the bond: "))
    bond_repayment = (interest_rate_monthly * house_value) / (1 - (1 + interest_rate_monthly) ** (- repayment_rate))
    print("\n \nYour monthly repayment will be: £" , bond_repayment )
# Else, if the user enters the word investment. Will ask about the deposit amount, interest rate, turning the float into percentile, asking the user to input the years they'd be commiting for.
elif user_input_lower == "investment":
    deposit = int(input("\nPlease enter how much you'd like to deposit: "))
    interest = float(input("\nNow enter your interest rate percentage : "))
    interest_rate = interest/100
    investment_years = int(input("\nPlease enter the amount of years you'd be commiting for: "))
    interest = input("\nPlease select between the 'compound' or 'simple' interest: ")
    interest_lower = interest.lower()
    print(interest_lower)
    # Creating a while loop condition where if the user input is neither 'simple' nor 'compound' to encourage correct input. If the input is either simple or compound, the code utilises the inputted numbers to execute a correct calculation for each of the seletions. Printing the user a total of their return for their selection.
    while interest_lower != "simple" and interest_lower != "compound":
        print("\nThis is not one of the permitted options. \nPlease try again")
        interest = input("\nPlease select between the 'compound' or 'simple' interest: ")
        interest_lower = interest.lower()
    if interest_lower == "simple":
        simple_interest_total = deposit * (1 + interest_rate * investment_years)
        print("\n \nThe total return for the simple interest will be £" , simple_interest_total )

    elif interest_lower == "compound":
        compound_interest_total = deposit * math.pow((1 + interest_rate), investment_years)
        print("\n \nThe total return for the compound interest will be £" , compound_interest_total )
