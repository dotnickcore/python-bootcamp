# A company has determined that its annual profit is typically 23 percent of total sales. Write
# a program that asks the user to enter the projected amount of total sales, then displays the
# profit that will be made from that amount.

projected = float(input("Enter the projected sales: "))
calculation = projected * 0.23
print("Profit $" + format(calculation, '.2f'))