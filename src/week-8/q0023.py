'''
[NOTE]: 
- Flags used for image file reading and writing: https://docs.opencv.org/3.4/d8/d6a/group__imgcodecs__flags.html#gga61d9b0126a3e57d9277ac48327799c80ae29981cfc153d3b0cef5c0daeedd2125
- Image Thresholding: https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html
- cv2.threshold: https://docs.opencv.org/3.4/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57
'''


import cv2
import numpy as np 
 
  
img = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE )
# cv2.imshow("Grayscale", img)
# cv2.waitKey(0)
  
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

print(np.unique(bw_img)) 
  
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
