# Interpolacion de Lagrange
# divisoresL solo para mostrar valores
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO , Datos de prueba
xi = np.array([1, 2,3,4,5])
fi = np.array([1, 4, 9,16 ,5])

# PROCEDIMIENTO
# Polinomio de Lagrange
n = len(xi)
x = sym.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype = float) #Cria uma lista de zeros (dtype = Float significa que eles tem ponto: 0.000)
for i in range(0,n,1):
    # Termino de Lagrange
    numerador = 1
    denominador = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador

    polinomio = polinomio + terminoLi*fi[i]
    divisorL[i] = denominador


# Simplificar o Polinomio
poli_simples = polinomio.expand() 
#Faz com que esse polinomio se torne uma função dentro do python (Chamada: px(3))
px = sym.lambdify(x,poli_simples) 

# Pontos para o Gráfico
tamanho = 100 #Serve para identificar a quantidade de elementos da linha 41
a = np.min(xi) #Retorna o valor minimo de xi
b = np.max(xi) #Retorna o valor maximo de xi
pxi = np.linspace(a,b,tamanho) #Cria uma lista com "Tamanho" elementos q vão de a até b no mesmo intervalo

#Coloca os valores de pxi na função para saber seus resultados e encontrar os resultados (Formato de lista)
pfi = px(pxi)
print(px(3))

# Saída
print('    Valores de Fi: ',fi)
print('divisores en L(i): ',divisorL)
print()
print('Polinomio de Lagrange, expresiones')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(poli_simples)

# Gráfica
plt.xlabel('X')
plt.ylabel('f(X)')
plt.title('Interpolação de Lagrange')

for y in range(0,len(xi)):
    plt.plot(xi[y],fi[y], 'o')
    plt.pause(1)

plt.plot(pxi,pfi) #Exibir a linha da equação

plt.show()
