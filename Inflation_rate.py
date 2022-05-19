# Inflation Rate Calculator
# This program solves for your personal inflation rate as compared to the same period last year.
# The calculator is based on the concept of spending more or less on the same expense segments this year or last year.
# The inflation rate percentage can be compared to the current national inflation rate.
# Check any credit card, bank, or payment statements from the most recent month and from a year prior.

# input your monthly expenses for the most recent month


foodExpenses = float(input("Input monthly food expense: "))
print ("Monthly Food Expense is: ", foodExpenses)


rentExpenses = float(input("Input rent or mortgage expenses: "))
print("Monthly Rent or Mortgage Expense is: ", rentExpenses)

utilityExpenses = float(input("Input utility expenses: "))
print("Monthly Utility Expense is: ", utilityExpenses)


vehicleExpenses = float(input("Input monthly vehicle, insurance, fuel, or transportation expenses: "))
print("Monthly Vehicle Expense is: ", vehicleExpenses)


entertainmentExpenses = float(input("Input entertainment expenses: "))
print("Monthly Entertainment Expenses is: ", entertainmentExpenses)


educationExpenses = float(input("Input education expenses: "))
print("Monthly Education Expense is: ", educationExpenses)


clothingExpenses = float(input("Input monthly clothing expenses: "))
print("Monthly Clothing Expense is: ", clothingExpenses)


miscellaneousExpenses = float(input("Input Monthly Miscellaneous Expenses: "))
print("Monthly Miscellaneous Expense is: ", miscellaneousExpenses)


# input your monthly expenses from a year prior to the most recent month

lyfoodExpenses = float(input("Input last year monthly food expense: "))
print("Last Year Monthly Food Expense is: ", lyfoodExpenses)


lyrentExpenses = float(input("Input last year rent or mortgage expenses: "))
print("Last Year Monthly Rent or Mortgage Expense is: ", lyrentExpenses)


lyutilityExpenses = float(input("Input last year utility expenses: "))
print("Last Year Monthly Utility Expense is: ", lyutilityExpenses)


lyvehicleExpenses = float(input("Input last year monthly vehicle, insurance, fuel, or transportation expenses: "))
print("Last Year Monthly Vehicle Expense is: ", lyvehicleExpenses)


lyentertainmentExpenses = float(input("Input last year entertainment expenses: "))
print("Last Year Monthly Entertainment Expenses is: ", lyentertainmentExpenses)


lyeducationExpenses = float(input("Input last year education expenses: "))
print("Last Year Monthly Education Expense is: ", lyeducationExpenses)


lyclothingExpenses = float(input("Input last year monthly clothing expenses: "))
print("Last Year Monthly Clothing Expense is: ", lyclothingExpenses)


lymiscellaneousExpenses = float(input("Input last year monthly miscellaneous expenses: "))
print("Last Year Monthly Miscellaneous Expense is: ", lymiscellaneousExpenses)
print()

# add the totals for this year
# addition

addThisYear = float(foodExpenses + rentExpenses + utilityExpenses + vehicleExpenses + entertainmentExpenses + educationExpenses + clothingExpenses + miscellaneousExpenses)
print("This is this years total expense amount: ", addThisYear)
print()

# add the totals for last year
# addition

addLastYear = float(lyfoodExpenses + lyrentExpenses + lyutilityExpenses + lyvehicleExpenses + lyentertainmentExpenses + lyeducationExpenses + lyclothingExpenses + lymiscellaneousExpenses)
print("This is last years total expense amount: ", addLastYear)
print()

# Subtract your total expenses for a year ago from the recent month.
# subtraction

subtractLastYearfromThisMonth = float(addThisYear - addLastYear)
print("The amount difference in spending: ", subtractLastYearfromThisMonth)
print()

# Divide the amount difference by the total expense from last year.
# The "f" in front and "{}"" is a way to place a variable in the middle of a sentence of string characters.

personalInflationRate = float(subtractLastYearfromThisMonth / addLastYear)
print(f"Your personal inflation rate is: {personalInflationRate} percent.")

