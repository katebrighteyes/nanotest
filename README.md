## nanotest

## gtk Error

sudo apt install libcanberra-gtk-module libcanberra-gtk3-module


# threshold

cv2.threshold(img, threshold_value, value, flag)

img:grayScale이고 threshold_value는 픽셀 문턱값이고 문턱값 이상이면 value로 바꾸어줍니다. 

 

flag에서도 다양한 종류가 존재합니다. 

 

cv2.THRESH_BINARY: threshold보다 크면 value이고 아니면 0으로 바꾸어 줍니다. 

cv2.THRESH_BINARY_INV: threshold보다 크면 0이고 아니면 value로 바꾸어 줍니다.   

cv2.THRESH_TRUNC: threshold보다 크면 value로 지정하고 작으면 기존의 값 그대로 사용한다. 

cv2.THRESH_TOZERO: treshold_value보다 크면 픽셀 값 그대로 작으면 0으로 할당한다. 

cv2.THRESH_TOZERO_INV: threshold_value보다 크면 0으로 작으면 그대로 할당해준다. 



출처: https://hoony-gunputer.tistory.com/265 [후니의 컴퓨터]
