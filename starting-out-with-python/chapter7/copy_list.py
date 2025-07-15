def main():
    # this will reference the same list in memory
    # Create a list.
    list1 = [1, 2, 3, 4]
    print(list1)
    print()
    # Assign the list to the list2 variable.
    list2 = list1
    print(list2)
    print()

    # creates a deep copy of the list
    # Create a list with values.
    list3 = [1, 2, 3, 4]
    print(list3)
    print()
    # Create an empty list.
    list4 = []
    # Copy the elements of list1 to list2.
    for item in list3:
        list4.append(item)

    print(list4)
    print()

main()