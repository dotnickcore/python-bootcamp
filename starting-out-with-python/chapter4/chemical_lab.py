DEGREE_LIMIT = 102.5

substance_temeperature = float(input("Enter the substance's temperature: "))

while substance_temeperature > DEGREE_LIMIT:
    print('The temperature is too high.')
    print('Turn the thermostat down and wait')
    print('5 minutes. Then take the temperature')
    print('again and enter it.')

    substance_temeperature = float(input('Enter the new Celsius temperature: '))

print('The temperature is acceptable.')
print('Check it again in 15 minutes.')