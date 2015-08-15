gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kp = sift.detect(gray, None)
img = cv2.drawKeypoints(gray, kp)
cv2.imwrite('sift_keypoints.jpg', img)

img = cv2.drawKeypoints(gray, kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)w

cv2.imwrite('sift_keypoints_circle.jpg', img)

kp,des = sift.detectAndCompute(gray, None)
img = cv2.drawKeypoints(gray, kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite('sift_keypoints_detect.jpg', img)
