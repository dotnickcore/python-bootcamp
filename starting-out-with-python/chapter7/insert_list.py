# This program demonstrates how to get the
# index of an item in a list and then replace
# that item with a new item.

def main():
    # Create a list with some names.
    names = ['James', 'Kathryn', 'Bill']

    # Display the list.
    print('The list before the insert:')
    print(names)

    # Insert a new name at element 0.
    names.insert(0, 'Joe')

    # Display the list again.
    print('The list after the insert:')
    print(names)

# Call the main function.
main()