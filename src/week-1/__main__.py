# I.1 Read RGB image.

# Python code to read image
import cv2
from matplotlib import pyplot as plt

FILE="./src/week-1/ironman.png"
NAME="Ironman"
 
# To read image from disk, we use
# cv2.imread function, in below method,
rgbImg = cv2.imread(FILE, cv2.IMREAD_COLOR)
 
# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
# cv2.imshow(NAME, img)
 
# # To hold the window on screen, we use cv2.waitKey method
# # Once it detected the close input, it will release the control
# # To the next line
# # First Parameter is for holding screen for specified milliseconds
# # It should be positive integer. If 0 pass an parameter, then it will
# # hold the screen until user close it.
# cv2.waitKey(0)
 
# # It is for removing/deleting created GUI window from screen
# # and memory
# cv2.destroyAllWindows()

# I.2. Convet image to Grayscale: 
grayImg = cv2.cvtColor(rgbImg, cv2.COLOR_BGR2GRAY)
# cv2.imshow(NAME,grayImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# II. Calculate & display histogram:
import numpy as np

def displayHist(file,mode,histSize):

	img = cv2.imread(file)
	b,g,r = cv2.split(img)
	fig = plt.figure(figsize=(8,4))

	ax = fig.add_subplot(121)
	ax.imshow(img[...,::-1])

	if mode=="RGB":
		ax = fig.add_subplot(122)
		for x, c in zip([b,g,r], ["b", "g", "r"]):
			xs = np.arange(histSize)
			ys = cv2.calcHist([x], [0], None, [histSize], [0,histSize])
			ax.plot(xs, ys.ravel(), color=c)
	else:
		ax = fig.add_subplot(122)
		xs = np.arange(histSize)
		ys = cv2.calcHist([img], [0], None, [histSize], [0,histSize])
		ax.plot(xs, ys.ravel())
     

	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	plt.show()

## II.1. Display RGB Historgram:  
# displayHist(FILE, "RGB",256)

## II.2. Display Grayscale Histogram:
# displayHist(FILE,"",256)

# III. Increase image quantization: 
histSizes=[8,32,64]
# for histSize in histSizes:
# 	displayHist(FILE, "RGB", histSize)
 
 
# IV. Display intensity profile: 
# import matplotlib.pyplot as plt
# import numpy as np
# from skimage.measure import profile_line
# from skimage import io

# # Load some image
# # I = io.imread(FILE, as_gray=True)
# I = io.imread(FILE)

# # Extract intensity values along some profile line
# p = profile_line(I, (45, 30), (160, 30))

# # Extract values from image directly for comparison
# i = I[45:161, 30]

# plt.plot(i)
# plt.ylabel('intensity')
# plt.xlabel('line path')
# plt.show()

STARTING_POINT=0
FINISH_POINT=100

ys=[]
for i in range(STARTING_POINT, FINISH_POINT):
	ys.append(rgbImg[i,10,0])
 
plt.plot(ys)
plt.show()
    


