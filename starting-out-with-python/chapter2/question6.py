# Write a program that asks the user to enter the amount of a purchase and the desired
# number of payment instalments. The program should add 5 percent to the amount to get
# the total purchase amount, and then divide it by the desired number of instalments, then
# display messages telling the user the total amount of the purchase and how much each
# instalment will cost.

INTEREST = 1.05

purchase_amount = float(input("Purchase Amount: "))
installments = int(input("Number of Instalments: "))

total_with_fee = purchase_amount * INTEREST
instalment_per_weekly = total_with_fee / installments

print("The total purchase amount: $" + format(total_with_fee, '.2f'))
print("Each instalment will cost: $" + format(instalment_per_weekly, '.2f'))