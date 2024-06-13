from numpy import loadtxt

data = loadtxt('data.csv', delimiter=',', skiprows=1)

x = data[:,0] * 0.01
print(x)
