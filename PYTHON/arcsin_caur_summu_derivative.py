import numpy as np
import matplotlib.pyplot as plt

def my_asin(x):
    k = 0
    a = x
    S = a
    
    while k < 500:
        k += 1
        R = ((2*k-1)**2*x*x)/((k*2)*(2*k+1))
        a = a*R
        S += a
        
    return S

a=-0.99999
b=0.99998
x = np.arange(a,b,0.05)
y = my_asin(x)
plt.plot(x,y)
plt.grid()
plt.show()
plt.plot(x,y)
plt.grid()
plt.show()
'''
n = len(x)
y_prim = []
for i in range(n-1):
    #print i, x[i], y[i]
    delta_y = y[i+1] - y[i]
    delta_x = x[i+1] - x[i]
    #y_prim = delta_y/delta_x
    #print y_prim
    y_prim.append(delta_y/delta_x)
plt.plot(x[:n-1],y_prim)

y_primprim = []
for i in range(n-2):
    delta_y_prim = y_prim[i+1] - y_prim[i]
    y_primprim.append(delta_y_prim/delta_x)

plt.plot(x[:n-2],y_primprim)
plt.show()
'''
