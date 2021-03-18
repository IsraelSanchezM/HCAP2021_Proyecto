#Bibliotecas importadas
import numpy as np

#Función de convolución
def convolucion(IOriginal, Kernel):
    #Variables:
    fr = len(IOriginal) - (len(Kernel) - 1)           #Número de filas de la matriz resultante
    cr = len(IOriginal[0]) - (len(Kernel[0]) - 1)     #Número de columnas de la matriz resultante 
    Res = np.zeros((fr, cr))                          #Matriz resultante

    #For para recorrer las filas
    for i in range(len(Res)):
        #For para recorrer las columnas
        for j in range(len(Res[0])):
            suma = 0  #Resultado de la multiplicación de la imagen con el Kernel
            #For para recorrer las filas del Kernel
            for m in range(len(Kernel)):
                #For para recorrer las columnas del Kernel
                for n in range(len(Kernel[0])):
                    suma += Kernel[m][n] * IOriginal[m + i][n + j] #Multiplicación de matrices
            Res[i][j] = suma #Sustituyendo el valor de la multiplicación en su celda correspondiente
    return Res #Se regresa la matriz resultante

#Probando la función
#Variables
K = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]                                                   #Kernel
I = [[2, 0, 1, 1, 1], [3, 0, 0, 0, 2], [1, 1, 1, 1, 1], [3, 1, 1, 1, 2], [1, 1, 1, 1, 1]]   #Imágen
In = np.array(I)  #Array de la imágen en numpy
Kn = np.array(K)  #Array del Kernel en numpy

R = convolucion(In, Kn) #Se hace la matriz resultante mandando a llamar la función de convolución
print(R)   #Se imprime la matriz resultante de la convoluciór
