import numpy as np
import cv2

def image_pp_segmentation(path):
    image_or = cv2.imread(path)
    image_before = cv2.imread(path)
    image_or = cv2.resize(image_or,(256,256))
    image_before = cv2.resize(image_before,(256,256))
    image2 = cv2.GaussianBlur(image_or,(5,5),0)
    image_f = np.array(image2)
    image = cv2.cvtColor(image2,cv2.COLOR_BGR2HSV)
    z = image.reshape((-1,3))
    Z = np.float32(z)
    cr = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
    k = 2
    ret,label,center = cv2.kmeans(Z,k,None,cr,10,cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    res = np.array(res)
    res2 = res.reshape((image.shape))

    mask = cv2.inRange(res2, (0,100,0), (173, 255, 170))
    imask = mask>0
    green = np.zeros_like(image,np.uint8)
    green[imask] = image[imask]


    res3 = green
    for i in range(256):
        for j in range(256):
            for k in range(3):
               if ((res3[i][j][k] == 0 or res3[i][j][k] == 0 or res3[i][j][k] == 0)):
                    image_or[i][j][k]=0


    print(center)
    return image_or,res2,image,image2,image_before
