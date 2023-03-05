#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index
def subset(input_list, start_index, end_index):
    return input_list[start_index:end_index]

#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size
def every_nth(input_list, step_size):
    if step_size > 0:
        return input_list[::step_size]
    else:
        return input_list

#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list
def unique(input_list):
    for element1 in input_list:
        count = 0
        for element2 in input_list:
            if element1 == element2:
                count = count + 1
        if count > 1:
            return False

    return True

#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list
def flatten(input_list):
    output_list = []
    if len(input_list) % 2 == 0:
        for i in range(0, len(input_list), 2):
            output_list.append([input_list[i], input_list[i+1]])
    else:
        for i in range(0, len(input_list)-1, 2):
            output_list.append([input_list[i], input_list[i+1]])
        output_list.append([input_list[i+1], ''])

    return output_list

#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args
def merge_lists(*args):
    output_list = []
    for element in args:
        output_list.append(element)
    return output_list

#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list
def reverse_tuples(input_list):
    output_list = []
    for element in input_list:
        output_list.append(element[::-1])
    return output_list

#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_tuplicates
#input parameters: input_list
def remove_duplicates(input_list):
    output_list = []
    output_list = list(dict.fromkeys(input_list))
    return output_list

#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list
def transpose(input_list):
    output_list = []
    
    return output_list

#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size
def split_into_chunks(input_list, chunk_size):
    output_list = []
    chunk_holder = []
    for element in input_list:
        if (len(chunk_holder) >= chunk_size):
            output_list.append(chunk_holder)
            chunk_holder = []
        chunk_holder.append(element)

    if chunk_holder is not None:
        output_list.append(chunk_holder)

    return output_list

#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict
def merge_dicts(*dict):
    output_dict = {k:v for d in (dict) for k,v in d.items()}
    return output_dict

#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list
def by_parity(input_list):
    output_dict = {
        'even': [],
        'odd': []
    }

    for element in input_list:
        if element % 2 == 0:
            output_dict['even'].append(element)
        else:
            output_dict['odd'].append(element)

    return output_dict

#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict
def mean_key_value(input_dict):
    output_dict = input_dict
    for key in output_dict:
        avg = sum(output_dict[key]) / len (output_dict[key])
        output_dict[key] = avg

    return output_dict
