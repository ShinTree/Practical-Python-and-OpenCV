import numpy as np                                                           #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import cv2                                                                   #Open CV2

def translate(image, x, y):                                                  #image이미지를 x좌표 x만큼, y좌표 y만큼 이동시키는 함수
    M = np.float32([[1, 0, x], [0, 1, y]])                                   #변환행렬 2X3의 float32 type의 numpy array [[1,0,X축 이동],[0,1,Y축 이동]]
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))     #shifted변수에 이미지저장 (위치가 변경된 이미지) (이미지, 변환행렬, 결과이미지크기)

    return shifted                                                           #shifted변수 리턴

###################################################################6-11
def resize(image, width = None, height = None, inter = cv2.INTER_AREA):      #image이미지를 
    dim = None                                                               #정해진 크기로 변환할거 아니라서 dim = None
    (h, w) = image.shape[:2]                                                 #h - image의 높이, w - image의 넓이

    if width is None and height is None:                                     #width, height의 입력값 없을 경우
        return image                                                         #image 리턴

    if width is None:                                                        #width 입력값이 없을경우(height 입력값이 있을 경우)
        r = height / float(h)                                                #변수 r에 height/h 저장
        dim = (int(w * r), height)                                           #변수 dim에 (정수(w*r), height) 저장

    else:                                                                    #그 외(height 입력값이 없을경우, width 입력값이 있을 경우)
        r = width / float(w)                                                 #변수 r에 width/w 저장
        dim = (width, int(h * r))                                            #변수 dim에 (width, 정수(h*r)) 저장
                 
    resized = cv2.resize(image, dim, interpolation = inter)                  #resized변수에 이미지저장 (크기가 변경된 이미지) (이미지, 변경할크기 튜플(가로,세로), 가로사이즈 배수, 세로사이즈 배수,
                                                                             #                                                 보간법(사이즈 줄일 때 : cv2.INTER_AREA, 사이즈 키울 때 : cv2.INTER_CUBIC, cv2.INTER_LINEAR))
    return resized                                                           #resized변수 리턴

###################################################################6-5
def rotate(image, angle, center = None, scale = 1.0):                        #image이미지를 angle만큼 회전하는 함수
    (h, w) = image.shape[:2]                                                 #h- image의 높이, w- image의 넓이

    if center is None:                                                       #center값이 없을경우,
        center = (w / 2, h / 2)                                              #center좌표 = w의 반, h의반

    M = cv2.getRotationMatrix2D(center, angle, scale)                        #변환행렬 생성(이미지의 중심좌표, 회전 각도(-는 반시계방향), scale factor)
    rotated = cv2.warpAffine(image, M, (w, h))                               #rotated변수에 이미지저장 (위치가 변경된 이미지) (이미지, 변환행렬, 결과이미지크기)

    return rotated                                                           #rotated변수 리턴
