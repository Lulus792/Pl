import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

k_B = 1.38e-23
h = 6.626e-34
c = 299792458
exp = 2.7182818284

def plank_strahlung(_Lambda, T):
    return 8*np.pi*h*c/(pow(_Lambda, 5)*(pow(exp, h*c/(_Lambda*k_B*T)) - 1))

wellenlaenge = np.linspace(1e-8, 3e-5, num=1000)
intensitat_1 = plank_strahlung(wellenlaenge, 750)
intensitat_2 = plank_strahlung(wellenlaenge, 800)
intensitat_3 = plank_strahlung(wellenlaenge, 850)

fig, ax = plt.subplots(figsize=(8, 8))
ax.text(max(wellenlaenge), max(intensitat_3), r'$\omega_{\nu}(\nu, T)=\frac{8\pi h c}{\lambda^5\left(e^{\frac{hc}{\lambda k_B T}}-1\right)}$', ha='right', va='top', fontsize='20')

plt.plot(wellenlaenge, intensitat_1)
plt.plot(wellenlaenge, intensitat_2)
plt.plot(wellenlaenge, intensitat_3)

plt.xlabel('Wellenlaenge in nm')
plt.ylabel('Intensitat in 'r'$\frac{\text{J}}{\text{s}}$')

#plt.legend()

plt.show()
