print("""##################################################
#                  MÉTODO DE SIMPSON
#Professor: Marcus Rocha
#Alunos: Gustavo, Naoki, Eduarda e Adriano 
##################################################""")
from sympy import *
import numpy as np
#Entrada
xf = Symbol('x')
fx = expand(input('Sua equação: '))
px = lambdify(xf,fx) 

a=0
b=1
n=1000

#N tem q ser impar
if int(n) % 2: 
    n += 1

x = np.linspace(a, b, n+1, dtype=float)
y = px(x)
h = (b - a) / n
Si = np.sum(y[1:-1:2]) 
Sp = np.sum(y[2:-1:2]) 

S = y[0] + 4 * Si + 2 * Sp + y[-1] 

#Saida
print(f"Resultado: {h * S / 3}")
