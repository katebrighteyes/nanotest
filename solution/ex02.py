from OpenCV_Functions import *

def processingSingleImage(image):
    result = imageCopy(image)
    result = convertColor(result, cv2.COLOR_BGR2HLS)
    h,l,s = splitImage(result)
    for i in range(0, 200):
        for j in range(0, 200):
            l2 = setPixel(l, i, j, 200)
    result = mergeImage(h,l2,s)
    result = convertColor(result, cv2.COLOR_HLS2BGR)
    return result

imagepath = "./solidWhiteCurve.jpg"

# cv2.IMREAD_COLOR
image_road = imageRead(imagepath, cv2.IMREAD_COLOR)


result = processingSingleImage(image_road)

imageShow("ex02", result, cv2.WINDOW_NORMAL)
