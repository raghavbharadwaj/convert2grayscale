import cv2
import sys

test1 = cv2.imread(sys.argv[1])
test1_white = cv2.cvtColor(test1,cv2.COLOR_BGR2GRAY)
cv2.imwrite('test1gray.png',test1_white)
cv2.imshow('color_image',test1)
cv2.imshow('gray_image',test1_white) 
cv2.waitKey(0)                 
cv2.destroyAllWindows()
 
