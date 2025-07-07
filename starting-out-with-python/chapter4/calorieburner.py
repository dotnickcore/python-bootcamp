"""
    Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
    uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
"""

def main():
    for minute in [10, 15, 20, 25, 30]:
        calculation = minute * 4.2
        message = "The amount of calories I burned after " + str(minute) + " minutes of exercise: " + str(calculation)
        print(message)

if __name__ == "__main__":
    main()