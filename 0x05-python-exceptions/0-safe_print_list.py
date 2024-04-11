#!/usr/bin/python3

def sfprnt_list(mlist = [], prnt_len = 0):
    ''' FUNCTION TO PRINT ANY LIST IN SAFE MODE '''
    # Loop through list to find list lenght
    list_len = 0
    for m in mlist:
        list_len += 1

    #try if prnt_len is not greater than list length
    try:
        mlist[prnt_len-1]
    except IndexError:
        #set prnt_len to list_len if try returns IndexError
        prnt_len = list_len

    for j in range(0, prnt_len):
        print(mlist[j], end = "")
    print("")
    return prnt_len
