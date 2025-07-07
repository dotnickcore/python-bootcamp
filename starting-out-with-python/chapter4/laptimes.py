"""
    Write a program that asks the user to enter the number of times that they have run around
    a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps.

    When the loop finishes, the program should display the time of their fastest lap, the time of
    their slowest lap, and their average lap time.
"""

def main():
    fastest_lap = 0.0
    slowest_lap = 0.0
    average_lap = 0.0
    total_lap_times = 0.0

    amount_of_laps = int(input("How many times did you run around the racetrack?: "))

    for lap in range(amount_of_laps):
        message = "What was your time for lap " + str(lap + 1) + ": "
        lap_time = float(input(message))

        total_lap_times = total_lap_times + lap_time

        if (fastest_lap == 0.0 or lap_time < fastest_lap):
            fastest_lap = lap_time

        if (slowest_lap == 0.0 or lap_time > slowest_lap):
            slowest_lap = lap_time

    average_lap = total_lap_times / float(amount_of_laps)

    print("")
    print("Laps Ran: " + str(amount_of_laps))
    print("Total Lap Time: "+ str(total_lap_times) + " seconds")
    print("===================================")
    print("")

    print("Fastest Lap: " + str(fastest_lap) + " seconds")
    print("Slowest Lap: " + str(slowest_lap) + " seconds")
    print("Average Lap: " + str(average_lap) + " seconds")

if __name__ == "__main__":
    main()