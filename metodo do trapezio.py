
import numpy as np
#Entrada
def f(x):
    return x**2
a = 0
b = 9
n = 9000

#Calculo
x = np.linspace(a, b, n+1, dtype=float)
y = f(x)
h = (b - a) / n
s = y[0] + 2.0 * np.sum(y[1:-1]) + y[-1]

#Saida
print(0.5 * h * s)
