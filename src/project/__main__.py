import cv2
import numpy as np

from matplotlib import pyplot as plt

PATH_BASE="."
PATH_DATA="./data"

img=cv2.cvtColor(cv2.imread(f"{PATH_DATA}/1_wIXlvBeAFtNVgJd49VObgQ.png_Salt_Pepper_Noise1.png", cv2.IMREAD_GRAYSCALE),cv2.COLOR_BGR2RGB)

imgs=[img]

for ksize in range(3,12,2):
    imgs.append(cv2.cvtColor(cv2.medianBlur(img,ksize), cv2.COLOR_BGR2RGB))

plt.figure(figsize=(5,5))
for i in range(6):
	ax=plt.subplot(3,2,i+1)	
	plt.imshow(imgs[i])
	plt.title(i*2+1)
	plt.axis("off")
 
plt.show()

"""
selected ksize: 7
"""

# TODO: notebook.

# Steps: 
# gray
# filter
# threshold
# connected

