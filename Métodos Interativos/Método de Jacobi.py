#====================================================================================
#======================== METODO DE ELIMINAÇÃO DE GAUSS-SEIDEL ======================
#====================================================================================
#        Alunos: Gustavo Tocantins, Kadu Naoki, Maria Eduarda, Marco Adriano
#====================================================================================

import math

def comparar(x,xk,eps):
    soma = 0
    zip_object = zip(x, xk)
    for list1_i, list2_i in zip_object:
        soma = soma + math.fabs(list1_i-list2_i)

    if (soma < eps):
        return True
    else:
        return False 

A = [[1, -1, 1],
     [ 1, 0,  0],
     [ 0, 2, 4]]

b = [4,1,-1]
eps = 0.00000007
intera = 1000
n = len(b)
sol = True
x = b.copy()
for i in range(0,n):
    if (math.fabs(A[i][i]) > 0.0):
        x[i] = b[i]/A[i][i]
    else:
        sol = False
        break

if (sol):
    print("Iteração 0")
    print("x = ",x)
xk = x.copy()
it = 0
 
while (it < intera):
    it = it + 1
    for i in range(1,n+1):
        s = 0
        for j in range(1,n+1):
            if ((i-1) != (j-1)):
                s = s + A[i-1][j-1]*x[j-1]

        xk[i-1] = (1/A[i-1][i-1])*(b[i-1]-s)
     
    print("Iteração: ",it)
    print(f"x = {x}")
    print("xk = ",xk)
      
    if comparar(x,xk,eps):
        x = xk.copy()
        break    
    x = xk.copy()

print('\n========== VALORES DE X ============')
for y in range(1,len(A[0])+1):
    print(f"x{y}: {x[y-1]}")
