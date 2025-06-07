# A customer in a store is purchasing five items. Write a program that asks for the price of
# each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

item_1 = float(input("Enter the price for item 1: "))
item_2 = float(input("Enter the price for item 2: "))
item_3 = float(input("Enter the price for item 3: "))
item_4 = float(input("Enter the price for item 4: "))
item_5 = float(input("Enter the price for item 5: "))

total = item_1 + item_2 + item_3 + item_4 + item_5

sales_tax = total * 0.07

total_amount = total + sales_tax

print("Sales Amount $" + format(total, '.2f'))
print("Sales Tax $" + format(sales_tax, '.2f'))
print("Total Amount $" + format(total_amount, '.2f'))