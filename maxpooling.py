import numpy as np

def maxpooling(Img):
    fr = len(Img)//2
    cr = len(Img[0])//2
    Res = np.zeros((fr, cr), np.uint8)

    i = 0
    for m in range(0, len(Img), 2):
        j = 0
        for n in range(0, len(Img[0]), 2):
            r = np.amax(Img[m: m + 2, n:n + 2])
            Res[i][j] = r
            j += 1
        i += 1        
    return Res
'''
I = [[1, 2, 3, 4], [5, 6, 7, 8], [4, 3, 2, 1], [1, 3, 7, 9]]
IA = np.array(I)
print(IA)
IR = maxpooling(IA)
print(IR)
'''
