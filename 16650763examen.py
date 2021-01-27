# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:12:13 2021

@author: Vic-gonz
"""
from scipy.optimize import differential_evolution
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
 
def fun(x):
    return(0.26 * (x[0] ** 2 + x[1] ** 2) - 0.48 * x[0] * x[1])

resultado=optimize.minimize(fun,(-10,10),bounds=((-10,10),(0,20)),method='TNC',tol=None)
x1=resultado.x
print(resultado.x)

plt.plot(x1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('optimizacion')
plt.show()