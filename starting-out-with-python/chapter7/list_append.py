# This program demonstrates how the append
# method can be used to add items to a list.

"""
    Method          Description
    append(item)    Adds item to the end of the list.

    index(item)     Returns the index of the first element whose value is equal to item.
                    A ValueError exception is raised if item is not found in the list.

    insert(index, item) Inserts item into the list at the specified index. When an item is
                        inserted into a list, the list is expanded in size to accommodate the new
                        item. The item that was previously at the specified index, and all the
                        items after it, are shifted by one position toward the end of the list.
                        No exceptions will occur if you specify an invalid index. If you specify
                        an index beyond the end of the list, the item will be added to the
                        end of the list. If you use a negative index that specifies an invalid
                        position, the item will be inserted at the beginning of the list.

    sort()          Sorts the items in the list so they appear in ascending order (from the
                    lowest value to the highest value).

    remove(item)    Removes the first occurrence of item from the list. A ValueError
                    exception is raised if item is not found in the list.
                    
    reverse()       Reverses the order of the items in the list.
"""

def main():
    # First, create an empty list.
    name_list = []

    # Create a variable to control the loop.
    again = 'y'

    # Add some names to the list.
    while again == 'y':
        # Get a name from the user.
        name = input('Enter a name: ')

        # Append the name to the list.
        name_list.append(name)

        # Add another one?
        print('Do you want to add another name?')
        again = input('y = yes, anything else = no: ')
        print()

    # Display the names that were entered.
    print('Here are the names you entered.')

    for name in name_list:
        print(name)

# Call the main function.
main()