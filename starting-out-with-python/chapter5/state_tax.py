"""
A retail company must file a monthly sales tax report listing the total sales for the month,
and the amount of state and county sales tax collected. The state sales tax rate is 5 percent
and the county sales tax rate is 2.5 percent. Write a program that asks the user to enter
the total sales for the month. From this figure, the application should calculate and display
the following:
• The amount of county sales tax
• The amount of state sales tax
• The total sales tax (county plus state)
"""

STATE_SALES_TAX = 0.05
COUNTY_SALES_TAX = 0.025

def main():
    total_state_sales_tax = 0.0
    total_county_sales_tax = 0.0
    total_sales_tax = 0.0

    while True:
        try:
            sales_quantity = int(input("Enter how many items were sold for this month: "))
            break
        except ValueError:
            print("Invalid Input: Error: Please enter a valid integer.")

    total_state_sales_tax = calculate_state_sales_tax(sales_quantity)
    total_county_sales_tax = calculate_county_sales_tax(sales_quantity)
    total_sales_tax = calculate_total_sales_tax(total_state_sales_tax, total_county_sales_tax)

    print("")
    print("=================================================")
    print(" Retail State and County Tax Calculation Results ")
    print("=================================================")
    print(" Total State Sales Tax: $", str(format(total_state_sales_tax, ".2f")))
    print(" Total Country Sales Tax: $", str(format(total_county_sales_tax, ".2f")))
    print(" Total Sales Tax: $", str(format(total_sales_tax, ".2f")))
    print("=================================================")
    print("")

def calculate_state_sales_tax(sales_quantity):
    return sales_quantity * STATE_SALES_TAX

def calculate_county_sales_tax(sales_quantity):
    return sales_quantity * COUNTY_SALES_TAX

def calculate_total_sales_tax(total_state_sales_tax, total_county_sales_tax):
    return total_county_sales_tax + total_state_sales_tax

main()