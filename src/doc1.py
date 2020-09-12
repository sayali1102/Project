import cv2
import numpy as np

image = cv2.imread('document-1.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image,(7,7),0)
image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,31,20)
#kernel = np.ones((18,18))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
image= cv2.erode(image,kernel,iterations=8)
#blur= cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
#image = cv2.GaussianBlur(image,(10,10),0)
#blur=cv2.blur(image,(5,5))
#blur= cv2.Canny(blur,100,200)



cv2.imwrite('blur2.png',image)
