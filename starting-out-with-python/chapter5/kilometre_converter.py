def main():
    result  = 0.0

    km_input = float(input("Enter your distance in km: "))

    result = convert_to_miles(km_input)

    print("This results in being ", str(format(result, ".2f")), "miles")

def convert_to_miles(kilometres):
    return kilometres * 0.6214

main()