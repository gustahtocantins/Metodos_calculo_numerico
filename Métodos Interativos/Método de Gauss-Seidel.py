import math
def comparar(y,xk,eps):
        soma = 0
        zip_object = zip(y, xk)
        for list1_i, list2_i in zip_object:
            soma = soma + math.fabs(list1_i-list2_i)

        if (soma < eps):
            return True
        else:
            return False 
            
def gaussSeidel(A, b,maxiter,eps):
    y = []
    VetorSolucao =[0]*len(A)
    iteracao = 0
    while iteracao < maxiter: #iteracao < iteracoes
        for i in range(len(A)):
            x = b[i] #7
            for j in range(len(A)):
                if i != j:
                    x -= A[i][j]*VetorSolucao[j]
            x /= A[i][i]
            VetorSolucao[i] = x
        iteracao += 1
        if(iteracao==1):
            y = VetorSolucao.copy()
        else:
            if comparar(y,VetorSolucao,eps):
                y = VetorSolucao.copy()
                return y
                break    
            y = VetorSolucao.copy()

A = [[ 1, 0,  0],
     [1, -1,  1],
     [ 1, 2, 4]]

b = [1,4,-1]
d = 1000000
coef = 0.00002
print(gaussSeidel(A,b,d,coef))
