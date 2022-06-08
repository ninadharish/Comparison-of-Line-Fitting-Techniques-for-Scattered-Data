import random
from lin_ls import *

def ransac(data):
    """Function to find the regression line with RANSAC

    Args: Data

    Returns: Parameters of line found using RANSAC
    """

    n = 10
    iter = 0
    max_iter = 50
    threshold = 0.02
    count = 0

    while iter < max_iter:

        rand_data = random.sample(data, k=len(data))
        maybeInliers = rand_data[:(n)]
        remain_list = rand_data[(n):]

        maybeModel = lin_ls(maybeInliers)
        
        count_temp = 0
        for i in range(len(remain_list)):
            if (((maybeModel[0] + maybeModel[1]*remain_list[i][0]) - remain_list[i][1]) < threshold):
                count_temp += 1

        if count_temp > count:
            bestModel = maybeModel
            count = count_temp
        
        iter += 1

    return bestModel
    