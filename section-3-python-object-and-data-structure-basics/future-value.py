future_value = float(input("Enter the desired future value: "))
annual_rate = float(input("Enter the annual interest rate: "))
num_of_years = float(input("Enter the number of years: "))

present_value = ((future_value)/((1 + annual_rate)**num_of_years))

print("Present Value: $", present_value)