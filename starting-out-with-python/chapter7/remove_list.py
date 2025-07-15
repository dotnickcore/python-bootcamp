# This program demonstrates how to use the remove
# method to remove an item from a list.

def main():
    # Create a list with some items.
    food = ['Pizza', 'Burgers', 'Chips']

    # Display the list.
    print('Here are the items in the food list:')
    print(food)

    # Get the item to change.
    item = input('Which item should I remove? ')

    try:
        # Remove the item.
        food.remove(item)

        # Display the list.
        print('Here is the revised list:')
        print(food)

    except ValueError:
        print('That item was not found in the list.')

    print()
    my_list = [1, 2, 3, 4, 5]
    print('Original order:', my_list)
    my_list.reverse()
    print('Reversed:', my_list)

    print()
    my_list2 = [1, 2, 3, 4, 5]
    print('Before deletion:', my_list2)
    del my_list2[2]
    print('After deletion:', my_list2)

# Call the main function.
main()