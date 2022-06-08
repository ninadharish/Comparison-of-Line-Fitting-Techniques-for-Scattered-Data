import numpy as np
import matplotlib.pyplot as plt

def tot_ls(data, x_mean, y_mean):
    """Function to find the regression with the Total Least Squares method

    Args:
        data: Data
        x_mean: Mean of Data(x)
        y_mean: Mean of Data(y)

    Returns: Parameters of line found using the Total Least Squares method
    """
    U = np.zeros((len(data),2))
    for i in range(len(data)):
        U[i][0] = data[i][0] - x_mean
        U[i][1] = data[i][1] - y_mean
    
    U_eig_val, U_eig_vec = np.linalg.eig(np.dot(U.T, U))

    N = U_eig_vec[:, np.argmin(U_eig_val)]
    d = N[0]*x_mean + N[1]*y_mean

    return N, d
    