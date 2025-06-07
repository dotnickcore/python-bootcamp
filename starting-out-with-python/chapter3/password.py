# • The uppercase characters A through Z are represented by the numbers 65 through 90.
# • The lowercase characters a through z are represented by the numbers 97 through 122.
# • When the digits 0 through 9 are stored in memory as characters, they are represented
# by the numbers 48 through 57. (For example, the string 'abc123' would be stored
# in memory as the codes 97, 98, 99, 49, 50, and 51.)
# • A blank space is represented by the number 32.

# This program compares two strings.
# Get a password from the user.
password = input('Enter the password: ')

# Determine whether the correct password
# was entered.
if password == 'prospero':
    print('Password accepted.')
else:
    print('Sorry, that is the wrong password.')