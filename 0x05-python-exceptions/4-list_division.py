#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for iter in range(list_length):
            try:
                new_list.append(my_list_1[iter] / my_list_2[iter])
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except TypeError:
                print("wrong type")
                new_list.append(0)
            except IndexError:
                print("out of range")
                new_list.append(0)
    finally:
        return new_list
