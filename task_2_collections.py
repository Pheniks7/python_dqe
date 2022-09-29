# import randrange function
from random import randrange

# create ALPHABET string for generating letters
ALPHABET = 'qwertyuiopasdfghjklzxcvbnm'


# define function for creating random length dict
def create_rand_dict():
    # create empty dict
    temp_dict = {}
    # dict length is a random value from 1 to 26 (max number of ALPHABET letters)
    while len(temp_dict) < randrange(1, 27):
        # randomly generate letter as key, number from 0 to 100 as a value - update temp_dict
        temp_dict[ALPHABET[randrange(26)]] = randrange(101)
    # return function result - random length dict
    return temp_dict


# define function for creating random length list of dicts
def create_rand_dict_list():
    # create empty lists
    temp_dict_list = []
    # randomly choose list length (from 2 to 10)
    for i in range(randrange(2, 10)):
        # add random dict to dict list in every iteration cycle
        temp_dict_list.append(create_rand_dict())
    # return function result - random length list of dicts
    return temp_dict_list


# define function for finding repeatable keys - input dict list
def get_common_keys(dict_list):
    # create empty lists
    common_list = []
    # join all the keys from all dicts into one list
    for dict_elem in dict_list:
        # extract keys from dict and transform them to list
        common_list = common_list + list(dict_elem.keys())
    # transform list to set - remove repeatable elements and iterate every element
    for key in set(common_list):
        # remove unique elements from the common_list - leave only repeatable ones
        common_list.remove(key)
    # return function result - repeatable elements set
    return set(common_list)


# define function for finding repeatable keys - input dict list
def get_common_keys_2(dict_list):
    # create empty sets with repeatable and unique elements
    common_set = set()
    unique_set = set()
    # iterate every dict in the list
    for dict_elem in dict_list:
        # extract keys from dict and transform them to set, define it as current set
        current_set = set(dict_elem.keys())
        # calculate unique_set and current_set intersection and join them to commot set
        common_set = common_set | (unique_set & current_set)
        # calculate current_set non-repeatable elements (minus) and join them to unique set
        unique_set = unique_set | (current_set - common_set)
    # return function result - repeatable elements set
    return common_set


# define function for dict merge - input dict and dict list
def merge_dict(common_dict, dict_list):
    # iterate every dict in the list
    for dict_elem in dict_list:
        # join dicts
        common_dict.update(dict_elem)
    # return function result - merged dict
    return common_dict


# define function for dict merge - input dict and dict list
def get_common_dict(dict_list, common_set):
    # create max value dict and copy input dict to change it
    max_value_dict = {}
    new_dict_list = dict_list.copy()
    # iterate every repeatable key element
    for key in common_set:
        # define temporary max_value and dict number for current key
        max_value = 0
        max_value_num = 0
        # iterate every dict in the list and get dict index for next operations
        for index, dict_elem in enumerate(new_dict_list, start=1):
            # in case of current key does not exist in current dict - pass
            if dict_elem.get(key) is not None:
                # in case of current value greater than previous one for current key
                if dict_elem.get(key) > max_value:
                    # redefine max_value and save dict number to max_value_num
                    max_value = dict_elem.get(key)
                    max_value_num = index
                else:
                    pass
                # remove key-value from current dict, leave in new_dict_list only non-repeatable keys
                dict_elem.pop(key)
        # once found max value and its dict number - create new key name with index and save it to the new dict
        key_index = key + '_' + str(max_value_num)
        max_value_dict[key_index] = max_value
    # return function result - run merge_dict function to merge all the dicts
    # considered to have only unique keys in all merged dicts
    return merge_dict(max_value_dict, new_dict_list)


# define function for dict sorting
def sort_dict(merged_dict):
    # create empty dict
    sorted_dict = {}
    # get key list
    keylist = list(merged_dict.keys())
    # sort key list
    keylist.sort()
    # iterate every key
    for key in keylist:
        # update the dict with sorted key-value
        sorted_dict[key] = merged_dict.get(key)
    # return function result - sorted dict
    return sorted_dict


# creating random length list of dicts and print every dict
a = create_rand_dict_list()
for index, dict_elem in enumerate(a, start=1):
    print('DICT_' + str(index), dict_elem)

# find repeatable keys (two ways) and print it
b = get_common_keys(a)
b_ = get_common_keys_2(a)
print('COMMON_SET\n', b)
print(b_)

# merge dicts with unique keys (max value found) and print it
c = get_common_dict(a, b)
print('COMMON_DICT\n', c)

# sort dict and print it
d = sort_dict(c)
print('SORTED_DICT\n', d)
