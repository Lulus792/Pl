import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def Voltage(x, a, b):
    return a*abs(np.cos(x*b))

data_file = pd.read_csv('data.csv', delimiter=',', dtype=float)
spannung = data_file['U'] 
theta = data_file['theta'] * np.pi/180

popc, popt = curve_fit(Voltage, theta, spannung)
a, b = popc

theta_fitt = np.linspace(-np.pi/2, np.pi/2, num=300)
spannung_fitt = Voltage(theta_fitt, a, b)

theta_fitt_spiegel = np.linspace(np.pi/2, 3*np.pi/2, num=300)
spannung_fitt_spiegel = spannung_fitt

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(7,7))

# Mit yerr und xerr kannst du den fehler einstellen welcher dan im plot
# angezeigt wird, xerr ist winkel und yerr spannung. color ist die Farbe des fehlers,
# und das fmt die Form des Messwerte Punkts wenn du das googelst bekomst du ganz viele 
# verschiedene optionen
ax.errorbar(theta, spannung, yerr=0.01, xerr=0.05, color='gray', fmt='.', label='Messwerte')# das macht einfach nur das in der Mitte nicht der Wert Null liegt (dadurch siehts
# besser aus) (meine meinung kannst es ja mal mit einem # davor auskommentieren und 
# schauen wie es aussienht)
ax.set_ylim([-0.05, 0.3])

# das sind die beiden plots fuer den fit am besten nicht anfassen
ax.plot(theta_fitt, spannung_fitt, label=r'$U=a\cdot\cos\left(\theta\cdot b\right)$''\n'r'$a='f'{round(a, 3)}'r'$, $b='f'{round(b, 3)}'r'$', color='orange')
ax.plot(theta_fitt_spiegel, spannung_fitt_spiegel, label='Fittfunktion als\nSpiegelung')

# hiermit kannst du den maximalen spannungs wert einstellen also sozusagen wie nah der 
# Rand an deinen Wert sein soll kannst ja einfach mal was anderes fuer 1.1 einsettzen 
# dann siehst du was es macht
ax.set_rmax((max(spannung)*1.1))

# das stellt ein in welchem abstand diese ringe im bild stehen und was fuer werte 
# dadrauf stehen das ist die beschriftung deiner y-achse
ax.set_rticks([0, 0.05, 0.1, 0.15, 0.2, 0.25])

# Der Winkel in welchem die zahlen von ax.set_rticks stehen
ax.set_rlabel_position(260)

# den rest kannst du ignorieren
ax.set_theta_zero_location('N')
ax.grid(True)

ax.legend(loc='lower left', bbox_to_anchor=(.75 + np.cos(29.8)/2, .74 + np.sin(-60.1)/2))

plt.savefig('Hertzscher_Dipol.svg')

plt.show()
