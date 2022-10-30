# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#import matplotlip.pyplot as plt
import numpy as np
import scipy
from scipy.stats import binom
from statsmodels.distributions.empirical_distribution import ECDF


def Empirical_F(X):
    X = sorted(X)
    Y,counts = np.unique(X,return_counts=True)
    n = len(X)
    p = 1/n
    col2 = []
    x = 0
    for i in range(len(Y)):
        if counts[i] == 1:
            x = x + p
            col2.append(x)
        else:
            k = counts[i]
            x = x + p*k
            for i  in range(k):
                col2.append(x)

    m = np.column_stack((X, col2))

    print(m)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = np.array([8,2,-13,4,-9,0,18,4,-5,10,1,-7,7,13,-5,-16,-9,18,-10,0])

    Empirical_F(x)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
