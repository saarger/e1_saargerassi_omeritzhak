# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import scipy
from scipy.stats import binom
import matplotlib.pyplot as plt



#Q2.a
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

#Q2.b
def make_observ():
    x = binom.rvs(n = 5, p  = 1/6,size =  20)
    return x

#Q2.c
def make_cdf():
    x = Empirical_F(make_observ())
    return x

#Q2.d
def ploting():
    m = make_cdf()
    print(m)
    x = m[:,0]
    y = m[:,1]
    plt.ylim(0,1)
    plt.step(x,y)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ploting()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
