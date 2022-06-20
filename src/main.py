import csv
import numpy as np
import matplotlib.pyplot as plt
from lin_ls import *
from tot_ls import *
from ransac import *
from cov import *
from norm import *


def plot():
    """Plot Linear Regression Output for the given data using all methods
    """

    filename = "../data/insurance.csv"

    age = []
    cost = []

    with open(filename) as csvfile:

        csvreader = csv.reader(csvfile)

        for row in csvreader:
                age.append(row[0])
                cost.append(row[6])

    del age[0]
    del cost[0]


    age = [float(i) for i in age]
    cost = [float(j) for j in cost]

    norm_age = norm(age)
    norm_cost = norm(cost)

    cov_matrix = np.array([[cov(age, age), cov(age, cost)], [cov(age, cost), cov(cost, cost)]])

    print('The covariance matrix cov_matrix =')
    print(cov_matrix)
    print('')

    cov_eig_val, cov_eig_vec = np.linalg.eig(cov_matrix)

    print('The eigen values of the covariance matrix are:')
    print(cov_eig_val)
    print('')
    print('The eigen vectors of the covariance matrix are:')
    print(cov_eig_vec)
    print('')

    origin = np.array([[np.mean(age)], [np.mean(cost)]])
    eig_vec1 = cov_eig_vec[:,0]
    eig_vec2 = cov_eig_vec[:,1]

    data = np.zeros((len(age),2))
    for i in range(len(age)):
        data[i] = [age[i], cost[i]]

    norm_data = np.zeros((len(norm_age),2))
    for i in range(len(norm_age)):
        norm_data[i] = [norm_age[i], norm_cost[i]]


    theta_lin = lin_ls(norm_data.tolist())

    tot_line, d = tot_ls(norm_data, np.mean(norm_age), np.mean(norm_cost))

    theta_ransac = ransac(norm_data.tolist())


    plt.scatter(age, cost)

    plt.quiver(*origin, eig_vec1[0], eig_vec1[1], color=['m'], scale=21)
    plt.quiver(*origin, eig_vec2[0], eig_vec2[1], color=['m'], scale=21)

    x_plot_norm = np.linspace(min(norm_age), max(norm_age), 50)
    x_plot = rev_norm(x_plot_norm, age)
    y_plot_lin = rev_norm((theta_lin[0] + theta_lin[1]*x_plot_norm), cost)
    y_plot_tot = rev_norm((d - (tot_line[0]*x_plot_norm))/(tot_line[1]), cost)
    y_plot_ransac = rev_norm((theta_ransac[0] + theta_ransac[1]*x_plot_norm), cost)

    plt.title('Plot', fontsize=18)
    plt.xlabel('Age', fontsize=14)
    plt.ylabel('Cost', fontsize=14)
    plt.plot(x_plot, y_plot_lin, color='r')
    plt.plot(x_plot, y_plot_tot, color='g')
    plt.plot(x_plot, y_plot_ransac, color='orange')
    plt.legend(['Standard Least Squares', 'Total Least Squares', 'RANSAC', 'Data Points', 'Eigen Vectors'], loc='upper left')
    plt.show()


if __name__ == "__main__":

    plot()
