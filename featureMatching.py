'''
    It is based on bruteforce
'''

import cv2
import numpy
import matplotlib.pyplot as plot

#media read
mainImage = cv2.imread('media/opencv-feature-matching-media.jpg', 0)
template  = cv2.imread('media/opencv-feature-matching-template.jpg', 0)

'''Define the similarities '''
orb = cv2.ORB_create()
#keypoints and descriptors
kp1, des1 = orb.detectAndCompute(template, None)
kp2, des2 = orb.detectAndCompute(mainImage, None)

bf      = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck= True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

processedImage = cv2.drawMatches(template, kp1, mainImage, kp2, matches[:10], None, flags=2)#matches[:10] shows first 10 matches

#media show
plot.imshow(processedImage)
plot.show()

