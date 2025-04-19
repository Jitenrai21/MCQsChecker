import cv2 
# To read image 
img = cv2.imread(r"C:\Users\ACER\OneDrive\Desktop\MCQs_Checker_Prep\images\mcqs_paper.jpg", cv2.IMREAD_COLOR) 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
ret, thresh = cv2.threshold(gray, 127, 255, 0) 
# finding the contours 
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
  
# take the first contour 
count = contours[0]

(x_axis,y_axis),radius = cv2.minEnclosingCircle(count) 
  
center = (int(x_axis),int(y_axis)) 
radius = int(radius) 
  
cv2.circle(img,center,radius,(0,255,0),2) 
cv2.imshow("Image",img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()