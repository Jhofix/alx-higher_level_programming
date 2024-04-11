#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    list_len=0
    for m in my_list:
        list_len += 1

    try:
        my_list[x-1]
    except IndexError:
        x = list_len

    for j in range(0, x):
        print(my_list[j], end="")
    print("")
    return x
