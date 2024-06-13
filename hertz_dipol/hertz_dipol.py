import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def Voltage(x, r, j):
    return r*(np.sin(x*j)**2)

def get_r_ticks(u):
    return np.linspace(min(u), max(u), num=5) 

data_file = pd.read_csv('data.csv', delimiter=',', dtype=float)
m_U = data_file['U'] 
theta = data_file['theta'] * np.pi/180

popc, popt = curve_fit(Voltage, theta, m_U)
r, j = popc

_Theta = np.arange(0, 2*np.pi, 0.1)
_U = Voltage(_Theta, r, j)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})#, figsize=(10,10))
ax.errorbar(theta, m_U, yerr=0.1, xerr=0.05, color='gray', fmt='.', label='Messwerte')
ax.plot(_Theta, _U, label=r'$U=a\cdot\sin^2\left(\theta\cdot b\right)$''\n'r'$a='f'{round(r, 3)}'r'$, $b='f'{round(j, 3)}'r'$', color='orange')

ax.set_rmax((max(m_U)*1.1))
ax.set_rticks(get_r_ticks(m_U))
#ax.set_rticks([0, 0.2, 0.4, 0.6, 0.8, 1])
ax.set_rlabel_position(180)
ax.set_theta_zero_location('N')
ax.grid(True)

#ax.set_title('Hertzscher Dipol', va='bottom')
ax.legend(loc='lower left', bbox_to_anchor=(.75 + np.cos(29.8)/2, .73 + np.sin(-60.1)/2))

plt.savefig('Hertzscher_Dipol.jpg')

plt.show()
