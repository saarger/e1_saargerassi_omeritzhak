# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#import matplotlip.pyplot as plt
import numpy as np
import scipy
from scipy.stats import binom
from statsmodels.distributions.empirical_distribution import ECDF
import matplotlib.pyplot as plt



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

    return m



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    X = binom.rvs(n = 5, p  = 1/6,size =  20)
    print(X)
    m = Empirical_F(X)

    y = m[:,1]
    y = np.transpose(y)
    print(y)
    print(X)
    plt.ylim(0,1)
    plt.step(X,y)
    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
