import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import curve_fit
import sys

def linear(x:list[float], m:float, n:float) -> list[float]:
    return m * x + n

data_file = np.loadtxt(sys.argv[1], delimiter=',', skiprows=1)
x:list[float] = data_file[:,0]
y:list[float] = data_file[:,1] 

popc, popt = curve_fit(linear, x, y)
m:float = popc[0]; n:float = popc[1]

x_line:list[float] = np.linspace(min(x)*0.9, max(x)*1.1, num=50)
y_line:list[float] = linear(x_line, m, n)

plt.xlabel('Spannung in kV')
plt.ylabel(r'Abstand in mm')

#plt.scatter(x,y, label='gemessenen Werte', marker='.')
plt.plot(x_line, y_line, '--', color='red', label=r'Linear fit: $m\dot x+n$''\n'r'$m=$'f'{round(m, 3)}, 'r'$n=$'f'{round(n,3)}')

x_error = 0.5 # 1% abweichung
y_error = 0.5 # +- 0.5mm

plt.errorbar(x, y, xerr=x_error, yerr=y_error, fmt='.', ecolor='gray', label='gemessenen Werte,\nmit abweichung')

plt.legend()
plt.savefig(sys.argv[2])
plt.show()
