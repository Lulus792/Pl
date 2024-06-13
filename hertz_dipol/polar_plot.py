import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def Voltage(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

@Voltage
def U(x, r, j):
    return r*(abs(np.sin(x))**j)

def get_r_ticks(r):
    return np.linspace(min(r), max(r), num=5)

theta = np.arange(0, 2*np.pi, 0.1)
r_dist = 304e-3 
j = 1.6
r = U(theta, r_dist, j) 

data_file = pd.read_csv('data.csv', delimiter=',', dtype=float)
_U:list[float] = data_file['U'] 
_Theta:list[float] = data_file['theta']


fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r, label=r'$U=r\cdot\mid\sin\left(\theta\right)\mid^j$''\n''$r=304\cdot10^{-3}$, $j=1,6$')
ax.plot(_Theta, _U, label='Messwerte')
ax.set_rmax((max(r)*1.1))
ax.set_rticks(get_r_ticks(r))
ax.set_rlabel_position(180)
ax.set_theta_zero_location('N')
ax.grid(True)

ax.set_title('Hertzscher Dipol', va='bottom')
ax.legend(loc='lower left', bbox_to_anchor=(.75 + np.cos(29.8)/2, .73 + np.sin(-60.1)/2))

plt.savefig('Hertzscher_Dipol.jpg')

plt.show()
