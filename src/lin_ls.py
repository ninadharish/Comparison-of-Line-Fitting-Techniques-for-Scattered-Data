import numpy as np


def lin_ls(data):
    """Function to find the regression with the Standard Least Squares method

    Args: Data

    Returns: Parameters of line found using the Linear Least Squares method
    """
    X_curve = np.zeros((len(data),2))
    Y_curve = np.zeros(len(data))
    for i in range(len(data)):
        X_curve[i][0] = 1
        X_curve[i][1] = data[i][0]
        Y_curve[i] = data[i][1]

    theta_lin = np.dot(np.linalg.inv(np.dot(X_curve.T, X_curve)), np.dot(X_curve.T, Y_curve))

    return theta_lin
