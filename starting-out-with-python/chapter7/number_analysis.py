"""
    Design a program that asks the user to enter a series of 20 numbers. The program should
    store the numbers in a list then display the following data:
        • The lowest number in the list
        • The highest number in the list
        • The total of the numbers in the list
        • The average of the numbers in the list
"""

def main():
    numbers_list = []

    numbers_list = return_numbers_in_list()

    lowest = return_lowest_number_in_list(numbers_list)

    highest = return_highest_number_in_list(numbers_list)

    total = return_total_number_in_list(numbers_list)

    average = return_average_number_in_list(total, len(numbers_list))

    print()
    print("Numbers in List:", numbers_list)
    print("Lowest In List:", lowest)
    print("Highest In List:", highest)
    print("Total:", total)
    print("Average:", str(format(average, ".2f")))
    print()

def return_numbers_in_list():
    list = []

    for x in range(20):
        while True:
            try:
                number = float(input(f"Enter a number {x+1} (int or float): "))
                list.append(number)
                break
            except ValueError:
                print("Invalid Input: Please Enter A Number")

    return list


def return_lowest_number_in_list(list):
    return min(list)

def return_highest_number_in_list(list):
    return max(list)

def return_total_number_in_list(list):
    total = 0.0

    for x in list:
        total += x

    return total

def return_average_number_in_list(total, length):
    return total / length

main()