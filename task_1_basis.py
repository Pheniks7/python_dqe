# import randrange function
from random import randrange


# define function for random list creation with parameters
def create_rand_list(numb, max_value):
    # create empty list
    rand_list = []
    # create a cycle with 'numb' iterations
    for i in range(numb):
        # add a random value (from 0 to 'max_value') to the list
        rand_list.append(randrange(max_value + 1))
    # return function result - the list with random values from 0 to 'max_value', length 'numb'
    return rand_list


# define function for list sorting
def sort_list(lst):
    # find list length
    length = len(lst)
    # create a cycle with iteration number equal to list length - 1
    for i in range(1, length):
        # internal cycle with iteration number equal to list length - i - 1
        for j in range(length - i):
            # check for reverse condition
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    # return function result - sorted list
    return lst


# define function for calculating average list value
def calc_average(lst):
    # apply try-except construction
    try:
        # divide list elements sum by list element count
        average = sum(lst) / len(lst)
    except ZeroDivisionError:
        # designate variable as NULL in case empty list
        average = None
    # return function result - average list value or NULL in case empty list
    return average


# define function for splitting the list into two list, with even and odd numbers
def split_even_odd(lst):
    # create empty lists
    even_list = []
    odd_list = []
    # run the cycle len(lst) times
    for i in range(len(lst)):
        # extract even numbers and add to the appropriate list
        if lst[i] % 2 == 0:
            even_list.append(lst[i])
        # the remainders add to the second list
        else:
            odd_list.append(lst[i])
    # return function result - average even_list value and average odd_list value
    return calc_average(even_list), calc_average(odd_list)


list_100 = create_rand_list(20, 20)
print(sort_list(list_100))
print(calc_average(list_100))
print(split_even_odd(list_100))
