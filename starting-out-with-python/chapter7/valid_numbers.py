"""
    Design a program that uses a loop to build a list named valid_numbers that contains only
    the numbers between 0 and 100 from the numbers list below. The program should then
    determine and display the total and average of the values in the valid_numbers list.
    numbers = [74, 19, 105, 20, −2, 67, 77, 124, −45, 38]
"""

def main():
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

    valid_numbers = return_valid_numbers(numbers)

    total = calculate_total(valid_numbers)

    average = calculate_average(total, len(valid_numbers))

    print()
    print("Valid Numbers:", valid_numbers)
    print("Total:", total)
    print("Average:", str(format(average, ".2f")))
    print()

def return_valid_numbers(numbers):
    valid_numbers = []

    for number in numbers:
        if 0 <= number <= 100:
            valid_numbers.append(number)

    return valid_numbers

def calculate_total(valid_numbers):
    total = 0.0

    for value in valid_numbers:
        total += value

    return total

def calculate_average(total, length):
    return total / length

main()