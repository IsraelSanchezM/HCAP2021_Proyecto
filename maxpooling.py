'''
Programa que cuenta con la función de maxpooling de una imagen y que cuenta con un ejemplo de la función
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

#Función de maxpooling
def maxpooling(Img):
    '''
    Función que se encarga de realizar el maxpooling con una imágen

    Parámetros: 
    Img = Matriz de la imagen a la que se le aplicará el maxpooling, debe de estar en escala de grises

    Retornos:
    Res = Matriz resultante de realizar el maxpooling en la imágen
    '''

    #Variables:
    fr = len(Img)//2                    #Número de filas de la matriz resultante
    cr = len(Img[0])//2                 #Número de columnas de la matriz resultante
    Res = np.zeros((fr, cr), np.uint8)  #Matriz resultante

    #For para recorrer las filas
    i = 0   #Índice de las filas de la matriz resultante
    for m in range(0, len(Img), 2):
        j = 0  #Índice de las columnas de la matriz resultante
        #Fot para recorrer las columnas
        for n in range(0, len(Img[0]), 2):
            r = np.amax(Img[m: m + 2, n:n + 2])  #Se hace el slice de la imágen y se encuentra el valor máximo
            if(i >= fr or j >= cr):  #Condición que impide que los valores de i y j se salgan de las dimensiones de la matris
                return Res
            else:    #De lo contrario sustituye el valor dentro de la celda correspondiente en la matriz resultante
                Res[i][j] = r
                j += 1
        i += 1  #Se le suma 1 a los índices para continuar iterando sobre la matriz resultante
    return Res
'''
#Probando la función
#Variables
I = [[1, 2, 3, 4], [5, 6, 7, 8], [4, 3, 2, 1], [1, 3, 7, 9]]    #Imágen
IA = np.array(I)  #Array de la imágen en numpy
print(IA)   #Se imprime el array 
IR = maxpooling(IA)     #Se hace la matriz resultante mandando a llamar la función del maxpooling
print(IR)     #Se imprime la matriz resultante del maxpooling
'''
