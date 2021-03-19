'''
Programa que cuenta con la función de convolución de una imágen y que posteriormente realiza un ejemplo de convolución
Autores: 
    * David Rodríguez Fragoso A01748760
    * Israel Sánchez Miranda A01378705
    * José Miguel García Gurtubay Moreno A01373750
    * Miguel Angel Juárez Dorantes A01753328
    * Omar Rodrigo Sorchini Puente A01749389
    * Paola Dorantes Calderón A01653108
18/03/2021
'''

#Bibliotecas importadas
import numpy as np #Numpy

#Función de convolución
def convolucion(IOriginal, Kernel):
    '''
    Función que se encarga de realizar la convolución a una imágen con un Kernel

    Parámetros:
    * IOriginal = Matriz de la imágen original a la que se le aplicará la convolución
    * Kernel = Matriz que servirá como el Kernel de la convolución de la imágen

    Retornos:
    * Res = Matriz resultante de realizar la convolución de la imágen
    '''

    #Variables:
    fr = len(IOriginal) - (len(Kernel) - 1)           #Número de filas de la matriz resultante
    cr = len(IOriginal[0]) - (len(Kernel[0]) - 1)     #Número de columnas de la matriz resultante 
    Res = np.zeros((fr, cr), np.uint8)                          #Matriz resultante

    #For para recorrer las filas
    for i in range(len(Res)):
        #For para recorrer las columnas
        for j in range(len(Res[0])):
            suma = 0  #Resultado de la multiplicación de la imágen con el Kernel
            #For para recorrer las filas del Kernel
            for m in range(len(Kernel)):
                #For para recorrer las columnas del Kernel
                for n in range(len(Kernel[0])):
                    suma += Kernel[m][n] * IOriginal[m + i][n + j] #Multiplicación de matrices
            if suma <= 255:
                Res[i][j] = round(suma) #Sustituyendo el valor de la multiplicación en su celda correspondiente
            else:
                Res[i][j] = 255
    return Res #Se regresa la matriz resultante
'''
#Probando la función
#Variables
K = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]                                                    #Kernel
I = [[2, 0, 1, 1, 1], [3, 0, 0, 0, 2], [1, 1, 1, 1, 1], [3, 1, 1, 1, 2], [1, 1, 1, 1, 1]]   #Imágen
In = np.array(I)  #Array de la imágen en numpy
Kn = np.array(K)  #Array del Kernel en numpy

R = convolucion(In, Kn) #Se hace la matriz resultante mandando a llamar la función de convolución
print(R)   #Se imprime la matriz resultante de la convolución
'''
