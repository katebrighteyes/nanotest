from OpenCV_Functions import *

def processingSingleImage(image):
    result = imageCopy(image)

    result = convertColor(result, cv2.COLOR_BGR2GRAY)
    MORPH_CROSS = imageMorphologyKernel(cv2.MORPH_CROSS, 5)
    result = imageMorphologyEx(result, cv2.MORPH_GRADIENT, MORPH_CROSS)
    height, width = image.shape[:2]
    src_pt1 = [int(width*0.35), int(height*0.65)]
    src_pt2 = [int(width*0.65), int(height*0.65)]
    src_pt3 = [width, height]
    src_pt4 = [0, height]
    dst_pt1 = [int(width*0.1),0]
    dst_pt2 = [int(width*0.9),0]
    dst_pt3 = [int(width*0.9),height]
    dst_pt4 = [int(width*0.1),height]
    #dst_pt3 = [int(width*0.8),height]
    #dst_pt4 = [int(width*0.2),height]
    src_pts = np.float32([src_pt1, src_pt2, src_pt3, src_pt4])
    dst_pts = np.float32([dst_pt1, dst_pt2, dst_pt3, dst_pt4])
    result = imagePerspectiveTransformation(result, src_pts, dst_pts)
    return result

imagepath = "./solidYellowCurve2.jpg"

# cv2.IMREAD_COLOR
image_road = imageRead(imagepath, cv2.IMREAD_COLOR)


result = processingSingleImage(image_road)

imageShow("ex03", result, cv2.WINDOW_NORMAL)
