#!/usr/bin/python3
# Function that devides element by elment 2 lists


def list_division(my_list_1, my_list_2, list_length):
    # Declaring a new list
    newList = []
    # Loop in list_length to devide the list1 by list2
    for i in range(list_length):
        # if the lists can be devided
        try:
            result = my_list_1[i] / my_list_2[i]
        # Handling erros if wrong type
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        # Handling erros if devided by zero
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        # Handling erros if out of range
        except IndexError:
            print("out of range")
            result = 0
        # Pushes the result to the newList
        finally:
            newList.append(result)
    # Returns the new list with number devided
    return newList
