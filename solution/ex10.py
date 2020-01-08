from OpenCV_Functions import *

def processingSingleImage(image):
    result = imageCopy(image)

    resultcolor = convertColor(image, cv2.COLOR_BGRA2BGR)
    result = convertColor(result, cv2.COLOR_BGR2GRAY)
    result = cannyEdge(result, 100, 200)
    height, width = result.shape[:2]
    src_pt1 = [int(width*0.35), int(height*0.65)]
    src_pt2 = [int(width*0.65), int(height*0.65)]
    src_pt3 = [width, height]
    src_pt4 = [0, height]
    dst_pt1 = [int(width*0.1),0]
    dst_pt2 = [int(width*0.9),0]
    dst_pt3 = [int(width*0.9),height]
    dst_pt4 = [int(width*0.1),height]
    src_pts = np.float32([src_pt1, src_pt2, src_pt3, src_pt4])
    dst_pts = np.float32([dst_pt1, dst_pt2, dst_pt3, dst_pt4])
    result = imagePerspectiveTransformation(result, src_pts, dst_pts)
    lines = houghLinesP(result, 1, np.pi/180, 40)

    empty = np.zeros((height, width), np.uint8)

    result_1 = drawHoughLinesP(empty, lines)
    result_2 = imagePerspectiveTransformation(result_1, dst_pts, src_pts)
    #result_3 = addImage(result_2, resultcolor)
    result_3 = addImage(result_2, image)

    return result_1, result_2, result_3


imagepath = "./solidYellowCurve2.jpg"

# cv2.IMREAD_COLOR
image_road = imageRead(imagepath, cv2.IMREAD_COLOR)


result_1, result_2, result_3 = processingSingleImage(image_road)

imageShow("ex10_res1", result_1, cv2.WINDOW_NORMAL)
imageShow("ex10_res2", result_2, cv2.WINDOW_NORMAL)
imageShow("ex10_res3", result_3, cv2.WINDOW_NORMAL)
