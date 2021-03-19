import cv2
import numpy as np
import maxpooling as mp
import convolucion as conv

def pipeline(img):
    IRGB = cv2.imread(img)
    IMGS = cv2.cvtColor(IRGB, cv2.COLOR_BGR2GRAY)
    Kernel = [[-1, -1, -1, -1, 0], [1, 1, 0, 0, 0], [1, 1, -1, -1, 0], [-1, 0, 0, 0, 1], [1, 1, 0, 0, -1]]
    K = np.array(Kernel)

    IR = conv.convolucion(IMGS, K)
    IR = mp.maxpooling(IR)
    for i in range(2):
        IR = conv.convolucion(IR, K)
        IR = mp.maxpooling(IR)

    cv2.imwrite('ICMPCS_David.jpg', IR)

pipeline('Grievous.jpg')
