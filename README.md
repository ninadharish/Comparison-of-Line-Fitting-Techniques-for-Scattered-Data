# Comparison of Line Fitting Techniques for Scattered Data

## Description

For a given series of scattered data points, line fitting is done to get a straight line that has the best fit. This can be done using methods like Linear Least Squares, Total Least Squares as well as Random sample consensus (RANSAC). For this scattered data, a line is fit using each of these methods for comparison. It is seen that RANSAC gives the best output since it rejects outliers and does not attempt to fit all points by working inside a threshold (as evident from the output).


## Data

The Medical Cost Personal Datasets by Kaggle ([Link](https://www.kaggle.com/datasets/mirichoi0218/insurance)) is used for this project. In this case, only the medical costs and the age of the individual is considered.


## Output

![alt text](/output/out.png)


## Getting Started

### Dependencies

<p align="left"> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>&ensp; </a>
<a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://www.codebykelvin.com/learning/python/data-science/numpy-series/cover-numpy.png" alt="numpy" width="40" height="40"/>&ensp; </a>
<a href="https://matplotlib.org/" target="_blank" rel="noreferrer"> <img src="https://static.javatpoint.com/tutorial/matplotlib/images/matplotlib-tutorial.png" alt="matplotlib" width="40" height="40"/>&ensp; </a>

* [Python 3](https://www.python.org/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)


### Executing program

* Clone the repository into any folder of your choice.
```
git clone https://github.com/ninadharish/Comparison-of-Line-Fitting-Techniques-for-Scattered-Data.git
```

* Open the repository and navigate to the `src` folder.
```
cd Comparison-of-Line-Fitting-Techniques-for-Scattered-Data/src
```

* Run the program.
```
python main.py
```


## Authors

👤 **Ninad Harishchandrakar**

* [GitHub](https://github.com/ninadharish)
* [Email](mailto:ninad.harish@gmail.com)
* [LinkedIn](https://linkedin.com/in/ninadharish)
