import cv2
import numpy as np


path = r"G:\codes\OpenCV_tests\test1.jpg"
img = cv2.imread(path)

width, height = 250,350
# [up and left point], [up and right point], [down and left point], [down and right point]
pts1 = np.float32([[622,590],[973,598],[412,851],[1236,845]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix,(width,height))

# draw tiny circles on the four points
for x in range(4):
    cv2.circle(img,(int(pts1[x][0]),int(pts1[x][1])),10,(0,0,255),cv2.FILLED)

point_warp = (200, 100)  # Replace this with the desired point from the warped perspective
cv2.circle(imgOutput,(int(point_warp[0]),int(point_warp[1])),10,(0,100,255),cv2.FILLED)

point_homogeneous = np.array([point_warp[0], point_warp[1], 1])

# Calculate the inverse of the transformation matrix
# inverse_matrix = np.linalg.inv(matrix)
inverse_matrix = cv2.getPerspectiveTransform(pts2,pts1)

# Apply the inverse transformation to the point
point_original_homogeneous = np.dot(inverse_matrix, point_homogeneous)

# Convert the result back to Cartesian coordinates
x_original = int(point_original_homogeneous[0] / point_original_homogeneous[2])
y_original = int(point_original_homogeneous[1] / point_original_homogeneous[2])

cv2.circle(img,(int(x_original),int(y_original)),10,(0,100,255),cv2.FILLED)

cv2.imshow("Original Image ", img)
cv2.imshow("Output Image ", imgOutput)
cv2.waitKey(0)