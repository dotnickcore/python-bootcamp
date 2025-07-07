"""
    Write a program that uses nested loops to collect data and calculate the average rainfall over
    a period of years. The program should first ask for the number of years. The outer loop will
    iterate once for each year. The inner loop will iterate twelve times, once for each month.
    Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
    After all iterations, the program should display the number of months, the total inches of
    rainfall, and the average rainfall per month for the entire period.
"""

MONTHS_IN_A_YEAR = 12

def main():
    total_january_rainfall_collected = 0.0
    total_february_rainfall_collected = 0.0
    total_march_rainfall_collected = 0.0
    total_april_rainfall_collected = 0.0
    total_may_rainfall_collected = 0.0
    total_june_rainfall_collected = 0.0
    total_july_rainfall_collected = 0.0
    total_august_rainfall_collected = 0.0
    total_september_rainfall_collected = 0.0
    total_october_rainfall_collected = 0.0
    total_november_rainfall_collected = 0.0
    total_december_rainfall_collected = 0.0

    total_rainfall_collected = 0.0

    januaryRainfall = []
    februaryRainfall = []
    marchRainfall = []
    aprilRainfall = []
    mayRainfall = []
    juneRainfall = []
    julyRainfall = []
    augustRainfall = []
    septemberRainfall = []
    octoberRainfall = []
    novemberRainfall = []
    decemberRainfall = []

    january_most_rainfall = 0.0
    january_least_rainfall = 0.0

    february_most_rainfall = 0.0
    february_least_rainfall = 0.0

    march_most_rainfall = 0.0
    march_least_rainfall = 0.0

    april_most_rainfall = 0.0
    april_least_rainfall = 0.0

    may_most_rainfall = 0.0
    may_least_rainfall = 0.0

    june_most_rainfall = 0.0
    june_least_rainfall = 0.0

    july_most_rainfall = 0.0
    july_least_rainfall = 0.0

    august_most_rainfall = 0.0
    august_least_rainfall = 0.0

    september_most_rainfall = 0.0
    september_least_rainfall = 0.0

    october_most_rainfall = 0.0
    october_least_rainfall = 0.0

    november_most_rainfall = 0.0
    november_least_rainfall = 0.0

    december_most_rainfall = 0.0
    december_least_rainfall = 0.0

    years = int(input("How many years do you want to collect rainfall?: "))

    for year in range(years):
        for month in range(MONTHS_IN_A_YEAR):
            month_match = month + 1
            message = "" 

            # break this into a seperate function
            match month_match:
                case 1:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month January: "
                case 2:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month February: "
                case 3:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month March: "
                case 4:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month April: "
                case 5:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month May: "
                case 6:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month June: "
                case 7:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month July: "
                case 8:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month August: "
                case 9:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month September: "
                case 10:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month October: "
                case 11:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month November: "
                case 12:
                    message = "Enter the amount of rain entered for year " + str(year + 1) + " for month December: "

            rainfall_collected = float(input(message))

            # break this into a seperate function
            match month:
                case 0:
                    januaryRainfall.append(rainfall_collected)
                case 1:
                    februaryRainfall.append(rainfall_collected)
                case 2:
                    marchRainfall.append(rainfall_collected)
                case 3:
                    aprilRainfall.append(rainfall_collected)
                case 4:
                    mayRainfall.append(rainfall_collected)
                case 5:
                    juneRainfall.append(rainfall_collected)
                case 6:
                    julyRainfall.append(rainfall_collected)
                case 7:
                    augustRainfall.append(rainfall_collected)
                case 8:
                    septemberRainfall.append(rainfall_collected)
                case 9:
                    octoberRainfall.append(rainfall_collected)
                case 10:
                    novemberRainfall.append(rainfall_collected)
                case 11:
                    decemberRainfall.append(rainfall_collected)

    # break this into a seperate function
    for i in januaryRainfall:
        total_january_rainfall_collected = total_january_rainfall_collected + i

        if (most_rainfall == 0.0 or i > most_rainfall):
            most_rainfall = i

        if (least_rainfall == 0.0 or i < least_rainfall):
            least_rainfall = i

    january_average_rainfall = total_january_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in January: "+ str(total_january_rainfall_collected) + "mm")
    print("===================================")
    print("")

    print("Most Rainfall In January: " + str(format(january_most_rainfall, ".2f")) + "mm")
    print("Least Rainfall In January: " + str(format(january_least_rainfall, ".2f")) + "mm")
    print("Average Rainfall In January: " + str(format(january_average_rainfall, ".2f")) + "mm")

    for i in februaryRainfall:
        total_february_rainfall_collected = total_february_rainfall_collected + i

    february_average_rainfall = total_february_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in February: "+ str(total_february_rainfall_collected) + " mm")
    print("===================================")
    print("")

    print("Most Rainfall In February: " + str(format(february_most_rainfall, ".2f")) + " mm")
    print("Least Rainfall In February: " + str(format(february_least_rainfall, ".2f")) + " mm")
    print("Average Rainfall In February: " + str(format(february_average_rainfall, ".2f")) + " mm")

    for i in marchRainfall:
        total_march_rainfall_collected = total_march_rainfall_collected + i

    march_average_rainfall = total_march_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in March: "+ str(total_march_rainfall_collected) + " mm")
    print("===================================")
    print("")

    print("Most Rainfall In March: " + str(format(march_most_rainfall, ".2f")) + " mm")
    print("Least Rainfall In March: " + str(format(march_least_rainfall, ".2f")) + " mm")
    print("Average Rainfall In March: " + str(format(march_average_rainfall, ".2f")) + " mm")

    for i in aprilRainfall:
        total_april_rainfall_collected = total_april_rainfall_collected + i

    april_average_rainfall = total_april_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in April: "+ str(total_april_rainfall_collected) + " mm")
    print("===================================")
    print("")

    print("Most Rainfall In April: " + str(format(april_most_rainfall, ".2f")) + " mm")
    print("Least Rainfall In April: " + str(format(april_least_rainfall, ".2f")) + " mm")
    print("Average Rainfall In April: " + str(format(april_average_rainfall, ".2f")) + " mm")

    for i in mayRainfall:
        total_may_rainfall_collected = total_may_rainfall_collected + i

    may_average_rainfall = total_may_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in May: "+ str(total_may_rainfall_collected) + " mm")
    print("===================================")
    print("")

    print("Most Rainfall In May: " + str(format(may_most_rainfall, ".2f")) + " mm")
    print("Least Rainfall In May: " + str(format(may_least_rainfall, ".2f")) + " mm")
    print("Average Rainfall In May: " + str(format(may_average_rainfall, ".2f")) + " mm")

    for i in juneRainfall:
        total_june_rainfall_collected = total_june_rainfall_collected + i

    june_average_rainfall = total_june_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in June: "+ str(total_june_rainfall_collected) + " mm")
    print("===================================")
    print("")

    print("Most Rainfall In June: " + str(format(june_most_rainfall, ".2f")) + " mm")
    print("Least Rainfall In June: " + str(format(june_least_rainfall, ".2f")) + " mm")
    print("Average Rainfall In June: " + str(format(june_average_rainfall, ".2f")) + " mm")

    for i in julyRainfall:
        total_july_rainfall_collected = total_july_rainfall_collected + i

    july_average_rainfall = total_july_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in July: "+ str(total_july_rainfall_collected) + " mm")
    print("===================================")
    print("")

    print("Most Rainfall In July: " + str(format(july_most_rainfall, ".2f")) + " mm")
    print("Least Rainfall In July: " + str(format(july_least_rainfall, ".2f")) + " mm")
    print("Average Rainfall In July: " + str(format(july_average_rainfall, ".2f")) + " mm")

    for i in augustRainfall:
        total_august_rainfall_collected = total_august_rainfall_collected + i

    august_average_rainfall = total_august_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in August: "+ str(total_august_rainfall_collected) + " mm")
    print("===================================")
    print("")

    print("Most Rainfall In August: " + str(format(august_most_rainfall, ".2f")) + " mm")
    print("Least Rainfall In August: " + str(format(august_least_rainfall, ".2f")) + " mm")
    print("Average Rainfall In August: " + str(format(august_average_rainfall, ".2f")) + " mm")

    for i in septemberRainfall:
        total_september_rainfall_collected = total_september_rainfall_collected + i

    september_average_rainfall = total_september_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in September: "+ str(total_september_rainfall_collected) + " mm")
    print("===================================")
    print("")

    print("Most Rainfall In September: " + str(format(september_most_rainfall, ".2f")) + " mm")
    print("Least Rainfall In September: " + str(format(september_least_rainfall, ".2f")) + " mm")
    print("Average Rainfall In September: " + str(format(september_average_rainfall, ".2f")) + " mm")

    for i in octoberRainfall:
        total_october_rainfall_collected = total_october_rainfall_collected + i

    october_average_rainfall = total_october_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in October: "+ str(total_october_rainfall_collected) + " mm")
    print("===================================")
    print("")

    print("Most Rainfall In October: " + str(format(october_most_rainfall, ".2f")) + " mm")
    print("Least Rainfall In October: " + str(format(october_least_rainfall, ".2f")) + " mm")
    print("Average Rainfall In October: " + str(format(october_average_rainfall, ".2f")) + " mm")

    for i in novemberRainfall:
        total_november_rainfall_collected = total_november_rainfall_collected + i

    november_average_rainfall = total_november_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in November: "+ str(total_november_rainfall_collected) + " mm")
    print("===================================")
    print("")

    print("Most Rainfall In Novembermber: " + str(format(november_most_rainfall, ".2f")) + " mm")
    print("Least Rainfall In November: " + str(format(november_least_rainfall, ".2f")) + " mm")
    print("Average Rainfall In November: " + str(format(november_average_rainfall, ".2f")) + " mm")

    for i in decemberRainfall:
        total_december_rainfall_collected = total_december_rainfall_collected + i

    december_average_rainfall = total_december_rainfall_collected / years

    print("")
    print("Total Rainfall Collected in December: "+ str(total_december_rainfall_collected) + " mm")
    print("===================================")
    print("")

    print("Most Rainfall In December: " + str(format(december_most_rainfall, ".2f")) + " mm")
    print("Least Rainfall In December: " + str(format(december_least_rainfall, ".2f")) + " mm")
    print("Average Rainfall In December: " + str(format(december_average_rainfall, ".2f")) + " mm")

if __name__ == "__main__":
    main()