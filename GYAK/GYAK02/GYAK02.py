import numpy as np

def create_array(size=(2,2)) -> np.array:
    return np.zeros(size)

def set_one(input_array) -> np.array:
    return np.fill_diagonal(input_array, 1)

def do_transpose(input_array) -> np.array:
    return np.transpose(input_array)

def round_array(input_array, round_size) -> np.array:
    return np.round(input_array, round_size)

def bool_array(input_array) -> np.array:
    return np.array(input_array, dtype=bool)

def invert_bool_array(input_array) -> np.array:
    return np.invert(np.array(input_array, dtype=bool))

def flatten(input_array) -> list:
    return np.ndarray.flatten(input_array)