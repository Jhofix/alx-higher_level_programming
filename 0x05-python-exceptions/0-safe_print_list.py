#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ''' FUNCTION TO PRINT ANY LIST IN SAFE MODE '''
    # Loop through list to find list lenght
    list_len = 0
    for m in my_list:
        list_len += 1

    #try if x is not greater than list length
    try:
        my_list[x-1]
    except IndexError:
        #set x to list_len if try returns IndexError
        x = list_len

    for j in range(0, x):
        print(my_list[j], end = "")
    print("")
    return x
