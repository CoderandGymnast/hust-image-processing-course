import csv
import cv2
import numpy as np

file = open('image.csv')
csvreader = csv.reader(file,  delimiter='\t')
img = []
for row in csvreader:
        img.append([int(e) for e in row])

img=np.array(img)
img=img.astype(np.uint8)

# gaussBlurImg = cv2.GaussianBlur(img,(3,3),0).astype(int)
# np.savetxt("out.csv", gaussBlurImg, delimiter=",", fmt="%.0f")

# medianImg=cv2.medianBlur(img, 3)
# np.savetxt("out.csv", medianImg, delimiter=",", fmt="%.0f")

kernel= np.array([[1,1,1],
                    [0,0,0],
                    [-1,-1,-1]])

img=cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
np.savetxt("out.csv",img, delimiter=",", fmt="%.0f")

