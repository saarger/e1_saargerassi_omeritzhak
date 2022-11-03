# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import numpy as np
import pandas as pd
import scipy
from scipy.stats import binom
import matplotlib.pyplot as plt




#Q2.a
from statsmodels.compat import pandas


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
    x = binom.rvs(n = 5, p  = 1/6,size =  1000)
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

#Q2.e
def creatY():
    y = binom.cdf([0,1,2,3,4,5],5,1/6)
    return y


#Q3.a
def func(df):
    sum = 0
    for i,r in df.iterrows():
        if r['Pathology'] == 2:
            sum+=1
    return sum/(df.index[-1]+1)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # m = make_cdf()
    # n = Empirical_F([0,1,2,3,4,5])
    #
    # x = m[:, 0]
    # y = m[:, 1]
    #
    # plt.ylim(0, 1)
    # plt.step(x, y)
    #
    # a = n[:, 0]
    # b = n[:, 1]
    #
    # plt.plot([0,1,2,3,4,5], [0.40187757,0.80375514,0.96450617,0.99665638,0.9998714,1. ])
    #
    # plt.show()
    #
    # for i in range(6):
    #     print(np.interp(i,x,y))

    df = pd.read_csv("/Users/oit/Downloads/appendicitis (1).csv")
    print(func(df))
    table = df.groupby(['Sex','Pathology']).count().reset_index().rename(columns = {'Age':'Count'})
    print(table)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
