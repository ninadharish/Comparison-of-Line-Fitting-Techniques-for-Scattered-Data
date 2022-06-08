import numpy as np

def cov(a, b):
    """Function to calculate the covariance of two arrays 'a' and 'b'

    Args:
        a: Data(x)
        b: Data(y)

    Returns: Covariance between Data(x) and Data(y)
    """

    if len(a) != len(b):
        return

    a_mean = np.mean(a)
    b_mean = np.mean(b)

    sum = 0

    for i in range(0, len(a)):
        sum += ((a[i] - a_mean) * (b[i] - b_mean))

    return sum/(len(a))
    