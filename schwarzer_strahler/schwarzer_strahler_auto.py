import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import sys

k_B = 1.38e-23
h = 6.626e-34
c = 299792458
exp = 2.7182818284

def plank_strahlung(_Lambda, D):
    return D*8*np.pi*h*c/(pow(_Lambda, 5)*(pow(exp, h*c/(_Lambda*k_B*T)) - 1))

for i in range(1, len(sys.argv)):
    fig, ax = plt.subplots(figsize=(8, 8))
    file = pd.read_csv(sys.argv[i], delimiter=',')
    x_data = file['x']
    y_data = file['y']
    T = file['T'][0]

    plt.scatter(x_data, y_data, label=r'$T=$'f'{T}')

    popt, popc = curve_fit(plank_strahlung, x_data, y_data)
    D = popt[0]

    x_data_fit = np.linspace(min(x_data), max(x_data), num=1000)
    y_data_fit = plank_strahlung(x_data_fit, D)

    D = format(D, '.2e')
    plt.plot(x_data_fit, y_data_fit, label='fit funktion\n'r'$D=$'f'{D}')

    plt.xlabel('Wellenlaenge in nm')
    plt.ylabel('Intensitat in 'r'$\frac{\text{J}}{\text{s}}$')

    plt.legend()

    plt.savefig(f'plot{i}.svg')
    plt.clf()

