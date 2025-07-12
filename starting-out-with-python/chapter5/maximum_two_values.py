"""
Write a function named max that accepts two integer values as arguments and returns the
value that is the greater of the two. For example, if 7 and 12 are passed as arguments to
the function, the function should return 12. Use the function in a program that prompts the
user to enter two integer values. The program should display the value that is the greater
of the two.
"""

def main():
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    result = determine_maximum_value(num1, num2)
    print(f"Between {num1} and {num2}, the maximum number was {result}")

def determine_maximum_value(num1, num2):
    return max(num1, num2)

main()