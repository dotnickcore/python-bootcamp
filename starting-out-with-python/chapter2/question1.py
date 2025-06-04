#
# Write a program that displays the following information:
# • Your name
# • Your address, with city, state, and ZIP
# • Your telephone number
# • Your job

name = input('What is your name: ')
address = input('What is your street address?: ')
city = input('What is your city?: ')
state = input('What is your state?: ')
postcode = input('What is your postcode?: ')
phone_number = input('What is your phone number?: ')
job = input('What is your job?: ')

print("Name:", name)
print("Address:", address + ", " + state + ", " + postcode)
print("Number:", phone_number)
print("Job:", job)