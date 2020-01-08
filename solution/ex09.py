from OpenCV_Functions import *

def processingSingleImage(image):
    result = imageCopy(image)

    result = convertColor(result, cv2.COLOR_BGR2GRAY)
    result = cannyEdge(result, 100, 200)
    height, width = result.shape[:2]
    #pt1 = (width*0.45, height*0.65)
    #pt2 = (width*0.55, height*0.65)
    #pt3 = (width, height*1.0)
    #pt4 = (0, height*1.0)
    #roi_corners = np.float32([[pt1, pt2, pt3,pt4]], dtype=np.int32)
    #result = polyROI(result, roi_corners)
#    pt1 = (int(width * 0.45), int(height * 0.65))
#    pt2 = (int(width * 0.55), int(height * 0.65))
    pt1 = (int(width * 0.35), int(height * 0.65))
    pt2 = (int(width * 0.65), int(height * 0.65))
    pt3 = (int(width), int(height))
    pt4 = (0, height)
    roi_poly = np.array([[pt1, pt2, pt3, pt4]], dtype = np.int32)
    roi_active = polyROI(result, roi_poly)
    lines = houghLinesP(roi_active, 1, np.pi/180, 40)
    result= drawHoughLinesP(image, lines)
    return result

imagepath = "./solidYellowCurve2.jpg"

# cv2.IMREAD_COLOR
image_road = imageRead(imagepath, cv2.IMREAD_COLOR)


result = processingSingleImage(image_road)

imageShow("ex03", result, cv2.WINDOW_NORMAL)
