from OpenCV_Functions import *

def drawRect(image, point1, point2, color=(255,0,0), thickness=3, lineType=cv2.LINE_AA):
    result = imageCopy(image)
    return cv2.rectangle(result, point1, point2, color, thickness, lineType);

def imageProcessing(frame):
    image = imageCopy(frame)
    height = image.shape[0]
    width = image.shape[1]
    pt1 = (0, int(height * 0.6))
    pt2 = (width, height)

    rect = drawRect(image, pt1, pt2, (255,0,0), 5)
    rect = drawText(rect, "OpenCV Processing", (10,50), cv2.FONT_HERSHEY_PLAIN, 2.5, (0,255,0),3)
    return rect

def Video2(openpath, savepath = "output.avi"):
    cap = cv2.VideoCapture(openpath)
    if cap.isOpened():
        print("Video Opened")
    else:
        print("Video Not Opened")
        print("Program Abort")
        exit()
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
    #out = cv2.VideoWriter(savepath, fourcc, fps, (width, height), True)
    cv2.namedWindow("Input", cv2.WINDOW_GUI_EXPANDED)
    cv2.namedWindow("Output", cv2.WINDOW_GUI_EXPANDED)
    import OpenCV_Functions
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
            # Our operations on the frame come here
            output = imageProcessing(frame)
            # Write frame-by-frame
            #out.write(output)
            # Display the resulting frame
            cv2.imshow("Input", frame)
            cv2.imshow("Output", output)
        else:
            break
        # waitKey(int(1000.0/fps)) for matching fps of video
        if cv2.waitKey(int(1000.0/fps)) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    #out.release()
    cv2.destroyAllWindows()
    return


road_video_01 = "./solidWhiteRight.mp4"

Video2(road_video_01, "output.mp4")
