import math

# Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a
# program that calculates the number of packages of hot dogs and the number of packages of
# hot dog buns needed for a cookout, with the minimum amount of leftovers. The program
# should ask the user for the number of people attending the cookout and the number of hot
# dogs each person will be given. The program should display the following details:
# • The minimum number of packages of hot dogs required
# • The minimum number of packages of hot dog buns required
# • The number of hot dogs that will be left over
# • The number of hot dog buns that will be left over

HOT_DOG_PACKAGES = 10
BUN_PACKAGES = 8

total_attendence = int(input("How many people will be attending?: "))
hotdog_per_person = int(input("How many hot dogs per person?: "))

total_hot_dogs = total_attendence * hotdog_per_person

hot_dog_packages_needed = math.ceil(total_hot_dogs / HOT_DOG_PACKAGES)
bun_packages_needed = math.ceil(total_hot_dogs / BUN_PACKAGES)

leftover_hot_dogs = (hot_dog_packages_needed * HOT_DOG_PACKAGES) - total_hot_dogs
leftover_buns = (bun_packages_needed * BUN_PACKAGES) - total_hot_dogs

print("Total Hotdogs Needed:", total_hot_dogs)
print("Hot Dog Packages Needed:", hot_dog_packages_needed)
print("Bun Packages Needed:", bun_packages_needed)
print("Hot Dog Packages Leftover:", leftover_hot_dogs)
print("Bun Packages Leftover", leftover_buns)