#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # create a new list to store the modified elements
    new_list = []

    # iterate through each element in the input list
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    # return the new list with the modified elements
    return new_lis
