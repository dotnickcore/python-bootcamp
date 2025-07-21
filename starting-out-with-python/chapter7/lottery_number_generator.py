"""
    Design a program that generates a seven-digit lottery number. The program should generate
    seven random numbers, each in the range of 0 through 9, and assign each number to a
    list element. (Random numbers were discussed in Chapter 5.) Then write another loop that
    displays the contents of the list.
"""

import random


def main():
    lotto_numbers = []

    lotto_numbers = return_lotto_numbers()

    display_list(lotto_numbers)

def return_lotto_numbers():
    lotto_numbers = []

    for count in range(7):
        number = random.randint(0, 9)
        lotto_numbers.append(number)

    return lotto_numbers

def display_list(lotto_numbers):
    print(lotto_numbers)

main()