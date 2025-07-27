"""
    Write a program that creates a dictionary containing the names of the Galilean moons of
    Jupiter as keys and their mean radiuses (in kilometers) as values. The dictionary should
    contain the following key-value pairs.

    The program should also create a dictionary containing the moon names and their surface
    gravities (in meters per second squared). The dictionary should contain the following keyvalue
    pairs.

    The program should also create a dictionary containing the moon names and their orbital
    periods (in days). The dictionary should contain the following key-value pairs.

    The program should let the user enter the name of a Galilean moon of Jupiter, then it
    should display the moon's mean radius, surface gravity and orbital period.
"""

LOOK_UP = 1
QUIT = 2

def main():
    dict = build_nested_dictionary()

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            lookup(dict)

def get_menu_choice():
    print()
    print('---------------------------')
    print('1. Look up a Galilean moon')
    print('2. Quit The Program')
    print()

    choice = int(input('Enter A Choice: '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice

def build_nested_dictionary():
    return {
        'io': {
            'mean_radius': 1821.6,
            'surface_gravity': 1.796,
            'orbital_period': 1.769
        },
        'iuropa': {
            'mean_radius': 1560.8,
            'surface_gravity': 1.314,
            'orbital_period': 3.551
        },
        'ganymede': {
            'mean_radius': 2634.1,
            'surface_gravity': 1.428,
            'orbital_period': 7.154
        },
        'callisto': {
            'mean_radius': 2410.3,
            'surface_gravity': 1.235,
            'orbital_period': 16.689
        }
    }
    

def lookup(moon_data):
    moon_name = input("Enter The Name of a Galilean Moon: ").lower()

    print()

    if moon_name in moon_data:
        print(f"'{moon_name}': {{")
        for key, value in moon_data[moon_name].items():
            print(f"    '{key}': {value},")
        print("}")
    else:
        print(f"No data found for moon: {moon_name}")

main()