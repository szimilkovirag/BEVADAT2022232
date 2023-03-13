import numpy as np

def column_swap(input_array) -> np.array:
    input_array[:,[0,1]] = input_array[:,[1,0]]
    return input_array

def compare_two_array(a1, a2) -> np.array:
    compared = a1 == a2
    return np.where(compared == True)[0]

def get_array_shape(input_array) -> int:
    return input_array.ndim

def encode_Y(input_array, n) -> np.array:
    result = np.zeros(n, input_array.max() + 1)
    for x in range(result.shape[1]):
        result[x][input_array[x]] = 1
    return result

def decode_Y(input_array) -> np.array:
    result = np.zeros(input_array.shape[1])
    for x in range(input_array.shape[1]):
        result[x] = np.where(input_array[x] == 1)[0][0]
    return result

def eval_classification(str_array, float_array) -> str:
    max_idx = np.where(float_array == np.max(float_array))[0][0]
    return str_array[max_idx]

def replace_odd_numbers(input_array) -> np.array:
    input_array[input_array%2 == 1] = -1
    return input_array

def replace_by_value(input_array, n) -> np.array:
    input_array[input_array >= n] = 1
    input_array[input_array < n] = -1
    return input_array

def array_multi(input_array) -> int:
    output = 1
    for x in input_array:
        output = output * x
    return output

def array_multi_2d(input_array) -> np.array:
    output = np.ones(input_array.shape[0])
    for x in range(input_array.shape[0]):
        for y in input_array[x]:
            output[x] = output[x] * y
    return output

def add_border(input_array) -> np.array:
    result = np.zeros(input_array.shape[1] + 2)
    return result

def list_days(date1, date2) -> list:
    output = []
    day = np.datetime64(date1 + '-01')
    while day < np.datetime64(date2 + '-01'):
        output.append(day)
        day = day + 1
    return output

def get_act_date() -> np.datetime64:
    return np.datetime64('today', 'D')

def sec_from_1970() -> int:
    date_from = np.datetime64('1970-01-01T00:00:00')
    current = np.datetime64('now')
    return (current - date_from).astype(int)
