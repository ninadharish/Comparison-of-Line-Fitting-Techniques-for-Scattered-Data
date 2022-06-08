import numpy as np

def norm(arr):
    """Function to normalize an array

    Args:
        arr: _description_

    Returns: Normalized array
    """
    norm_arr = np.empty(len(arr))
    for i in range(len(arr)):
        norm_arr[i] = ((arr[i] - np.min(arr))/(np.max(arr) - np.min(arr)))
    
    return norm_arr


def rev_norm(y, arr):
    """Function to reverse normalise a value with respect to an array

    Args:
        y (_type_): Data value to be reverse-normalized
        arr (_type_): Array of normalized data

    Returns: Reverse-normalized data value
    """
    y_new = ((y*(np.max(arr) - np.min(arr))) + np.min(arr))

    return y_new
    