import numpy as np 
import cv2

testImg= 'document.png'
tempImg= 'blur2.png'
######## Extracting details from image and writing into another

image = cv2.imread(testImg)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image,(5,5),0)
image = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,31,20)
#kernel = np.ones((18,18))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
image= cv2.erode(image,kernel,iterations=3)
#blur= cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
#image = cv2.GaussianBlur(image,(10,10),0)
#blur=cv2.blur(image,(5,5))
#blur= cv2.Canny(blur,100,200)
cv2.imwrite(tempImg,image)


######## Using the created temp image

img=cv2.imread(tempImg)
original=cv2.imread(testImg)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# binarize the image
img = cv2.GaussianBlur(img,(17,17),0)
ret, bw = cv2.threshold(gray, 128, 255, 
cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# find connected components

connectivity = 40
nb_components, output, stats, centroids =cv2.connectedComponentsWithStats(bw, connectivity, cv2.CV_32S)
sizes = stats[1:, -1]; nb_components = nb_components - 1
min_size = 10250 #threshhold value for objects in scene
img2 = np.zeros((img.shape), np.uint8)
for i in range(0, nb_components+1):
    # use if sizes[i] >= min_size: to identify your objects
    color = np.random.randint(255,size=3)
    # draw the bounding rectangele around each object
    cv2.rectangle(original, (stats[i][0],stats[i][1]),(stats[i][0]+stats[i][2],stats[i][1]+stats[i][3]), (0,255,0), 2)
    img2[output == i + 1] = color
cv2.imwrite('image.png',original)

###### Open image.png to check results 





