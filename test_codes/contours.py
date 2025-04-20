# for b in bubble_info:
#     cv2.drawContours(question_img, [b[3]], -1, (255, 0, 0), 1)  # All
# cv2.drawContours(question_img, [darkest[3]], -1, (0, 255, 0), 2)  # Selected

# # Better thresholding (Otsu)
# ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# # finding the contours 
# contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
  
# # Loop through contours and draw only circular ones (like bubbles)
# for cnt in contours:
#     area = cv2.contourArea(cnt)
#     if area < 500 or area > 3000:
#         continue  # Skip small or large noise

#     perimeter = cv2.arcLength(cnt, True)
#     circularity = 4 * 3.14 * (area / (perimeter * perimeter + 1e-5))  # Add small number to avoid division by zero

#     if 0.7 < circularity < 1.2:  # Only circular shapes
#         (x, y), radius = cv2.minEnclosingCircle(cnt)
#         center = (int(x), int(y))
#         radius = int(radius)
#         cv2.circle(img, center, radius, (0, 255, 0), 2)
  
# # Show result
# cv2.imshow("Detected Bubbles", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()