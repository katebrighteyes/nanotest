from OpenCV_Functions import *

def processingSingleImage(image):
    result = imageCopy(image)
    for i in range(0, 200):
        for j in range(0, 200):
            result = setPixel(result, i, j, [0,0,0])
    return result

imagepath = "./solidWhiteCurve.jpg"

# cv2.IMREAD_COLOR
image_road = imageRead(imagepath, cv2.IMREAD_COLOR)


result = processingSingleImage(image_road)

imageShow("ex01", result, cv2.WINDOW_NORMAL)
