# Write a program that calculates the total amount of a meal purchased at a restaurant. The
# program should ask the user to enter the charge for the food, then calculate the amounts
# of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

TIP_PERCENT = 0.18
SALES_TAX = 0.07

food_amount = float(input("Enter the total amount of food: "))

sales_tax_calcuation = food_amount * SALES_TAX
tip_calculation = food_amount * TIP_PERCENT
total_calculation = food_amount + sales_tax_calcuation + tip_calculation

print("Amount before Tip and Tax: $" + format(food_amount, '.2f'))
print("Tip: $" + format(tip_calculation, '.2f'))
print("Sales Tax $" + format(sales_tax_calcuation, '.2f'))
print("Total Amount: $" + format(total_calculation, '.2f'))
