import csv
import cv2
import numpy as np

file = open('image.csv')
# file = open('.\\src\\week-3\\image.csv')
csvreader = csv.reader(file,  delimiter='\t')
img = []
for row in csvreader:
        img.append([int(e) for e in row])

img=np.array(img)
img=img.astype(np.float32)

# gaussBlurImg = cv2.GaussianBlur(img,(3,3),0).astype(np.float32)
# np.savetxt("out.csv", gaussBlurImg, delimiter=",", fmt="%.0f")
# print(gaussBlurImg)

# medianImg=cv2.medianBlur(img, 5)
# np.savetxt("out.csv", medianImg, delimiter=",", fmt="%.0f")
# print(medianImg)

# print("...")

kernel= np.array([[1, 0, -1],
                    [1,0,-1],
                    [1,0,-1]])
kernel.astype(np.float32)

img=cv2.filter2D(src=img, ddepth=-1, kernel=kernel,borderType=cv2.BORDER_REFLECT)
np.savetxt("out.csv",img, delimiter=",")
print(img)

