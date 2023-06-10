#Alunos: Gustavo Tocantins, Kadu Naoki, Maria Eduarda, Marco Adriano

#===============================================================================
#======================== METODO DE ELIMINAÇÃO DE GAUSS ========================
#===============================================================================
# m1 = Matriz do primeiro sistema       | m2 = Matriz do segundo sistema
# n = quantidade de linhas da matriz    | c = quantidade de colunas
# matriz_1 = Valores de x do sistema (1)| matriz_1 = Valores de x do sistema (2)  
#x = valores de x

from tkinter import *
matriz = [[1,0,0,1],
          [1,-1,1,4],
          [1,2,4,-1]]

n = len(matriz)
c = len(matriz[0]) #5

#====== Pivoteamento ======
for p in range(0,n):
    for r in range(p+1,n): #1 Valor da segunda linha, 3 valor da terceira linha
        fator = -matriz[r][p]/matriz[p][p]
        for z in range(p,c): #Valor de cada linha
            matriz[r][z] = matriz[r][z]+fator*matriz[p][z] 

#Exibir Matriz pivoteada
print("======== MATRIZ PIVOTEADA ========")
for y in matriz:
    print(y)

 #Quantidade de linhas q a matriz tem
x = [0]*n #Criar uma lista com n zeros

x[n-1] = matriz[n-1][c-1]/matriz[n-1][c-2] #Valor de Xn

for i in range(n-1,0,-1): #Contagem regressiva (2,1)
    s = 0 #Somatorio
    for j in range(i+1,n+1): #J varia de (3,2,3)
        s = s + matriz[i-1][j-1]*x[j-1]

    x[i-1] = (matriz[i-1][n]-s)/(matriz[i-1][i-1])

#Exibir valores de X

cor_fundo = "#191970" #Azul escuro
win = Tk() #Criar janela
win.title("Eliminação de Gauss") #Titulo da janela
win["bg"] = cor_fundo
win.geometry("500x300") #Tamanho da janela

#inicio
inicio = Frame(win) #Criar um quadro
inicio["bg"] = cor_fundo
inicio.pack() #Mostra o quadro

titulo1 = Label(inicio, text="VALORES DE X", font="arial 40 bold",fg="yellow", bg=cor_fundo) #criar texto "VALORES DE X"
titulo1.pack() #exibir texto

for e in range(0,len(x)): # Comando para saber a posição dos valores de x dentro da lista X
    exibir_mat = Label(inicio, text=f"X{e+1}: {x[e]}",font="Courier 30 italic", bg=cor_fundo, fg="white") #Criar texto
    exibir_mat.pack() #exibir texto


win.mainloop()
