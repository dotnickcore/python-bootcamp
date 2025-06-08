TAX_RATE = 0.0065

sential_value = -1

while sential_value != 0:
    property_value = float(input("Enter the property value: "))

    propert_tax = property_value * TAX_RATE

    print("Property Tax: $", format(propert_tax, '.2f'))

    sential_value = int(input("Would you like to do another?: (press 0 to end)"))