import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import sys

fig, ax = plt.subplots(figsize=(8, 8))

for i in range(1, len(sys.argv)):
    file = pd.read_csv(sys.argv[i], delimiter=',')
    x_data = file['x']
    y_data = file['y']
    T = file['T'][0]
    plt.plot(x_data, y_data, label=r'$T=$'f'{T}')


plt.xlabel(r'Wellenlaenge in $\mu$m')
plt.ylabel('Intensitat in 'r'$\frac{\text{J}}{\text{s}}$')

plt.legend()

plt.show()
