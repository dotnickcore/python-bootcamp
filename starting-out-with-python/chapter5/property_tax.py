"""
    A county collects property taxes on the assessment value of property, which is 60 percent of
    the property’s actual value. For example, if an acre of land is valued at $10,000, its assessment
    value is $6,000. The property tax is then 72¢ for each $100 of the assessment value.
    The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the
    actual value of a piece of property and displays the assessment value and property tax.
"""

ASSEMENT_PERCENTAGE = 0.60
PROPERTY_TAX_CENTS = 0.72
PROPERTY_TAX_THRESHOLD = 100

def main():
    property_value = float(input("Enter the property value: "))

    assessment_value = calculate_assessment_value(property_value)

    property_tax = calculate_property_tax(assessment_value)

    print("")
    print("================================")
    print("Property Value: $", str(format(property_value, ".2f")))
    print("Assessment Value: $", str(format(assessment_value, ".2f")))
    print("Property Tax: $", str(format(property_tax, ".2f")))
    print("================================")

def calculate_assessment_value(property_value):
    return property_value * ASSEMENT_PERCENTAGE

def calculate_property_tax(assessment_value):
    return (assessment_value / PROPERTY_TAX_THRESHOLD) * PROPERTY_TAX_CENTS

main()