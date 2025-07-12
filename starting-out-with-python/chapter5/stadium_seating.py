"""
    There are three seating categories at a stadium. Class A seats cost $350, Class B seats cost
    $120, and Class C seats cost $75. Write a program that asks how many tickets for each class
    of seats were sold, then displays the amount of income generated from ticket sales.
"""

CLASS_A_TICKET_COST = 350
CLASS_B_TICKET_COST = 120
CLASS_C_TICKET_COST = 75

def main():
    total_sales = 0.0

    while True:
        try:
            class_A_quantity = int(input("Enter how Class A tickets were sold: "))
            break
        except ValueError:
            print("Invalid Input: Please Enter A Integer")

    while True:
        try:
            class_B_quantity = int(input("Enter how Class B tickets were sold: "))
            break
        except ValueError:
            print("Invalid Input: Please Enter A Integer")

    while True:
        try:
            class_C_quantity = int(input("Enter how Class C tickets were sold: "))
            break
        except ValueError:
            print("Invalid Input: Please Enter A Integer")

    class_A_sales =  calculate_class_A_ticket_sales(class_A_quantity)
    class_B_sales =  calculate_class_A_ticket_sales(class_B_quantity)
    class_C_sales =  calculate_class_A_ticket_sales(class_C_quantity)
    total_sales = class_A_sales + class_B_sales + class_C_sales

    print("")
    print("===========================================")
    print("Class A Ticket Sales: $", str(format(class_A_sales, ".2f")))
    print("Class B Sales: $", str(format(class_B_sales, ".2f")))
    print("Class C Sales: $", str(format(class_C_sales, ".2f")))
    print("Total Ticket Sales: $", str(format(total_sales, ".2f")))
    print("===========================================")
    print("")

def calculate_class_A_ticket_sales(quantity_of_tickets):
    return quantity_of_tickets * CLASS_A_TICKET_COST

def calculate_class_B_ticket_sales(quantity_of_tickets):
    return quantity_of_tickets * CLASS_B_TICKET_COST
    
def calculate_class_C_ticket_sales(quantity_of_tickets):
    return quantity_of_tickets * CLASS_C_TICKET_COST

main()