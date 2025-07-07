"""
    A bug collector collects bugs every day for five days. Write a program that keeps a running
    total of the number of bugs collected during the five days. The loop should ask for the
    number of bugs collected for each day, and when the loop is finished, the program should
    display the total number of bugs collected.
"""

def main():
    totalBugsCollected = 0

    for day in range(5):
        message = 'How many bugs did you catch on day ' + str(day + 1) + ': '
        bugsCollected = int(input(message))
        totalBugsCollected = totalBugsCollected + bugsCollected

    # Display the total amount of bus collected.
    print('The total is', totalBugsCollected)

if __name__ == "__main__":
    main()