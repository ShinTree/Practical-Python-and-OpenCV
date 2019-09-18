import numpy as np                                                              #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import argparse                                                                 #아규먼트 입력을 위한 argparse
import imutils                                                                  #translate함수를 쓰기위한 imutils(사용자라이브러리)
import cv2                                                                      #Open CV2

ap = argparse.ArgumentParser()                                                  #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")   #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                    #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                               #args변수의 image에 대응하는 사진경로 불러와서 image 변수에 이미지 저장
cv2.imshow("Original", image)                                                   #Origianl이라는 이름으로 image이미지 출력

M = np.float32([[1, 0, 25], [0, 1, 50]])                                        #변환행렬 2X3의 float32 type의 numpy array [[1,0,X축 이동],[0,1,Y축 이동]]
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))            #shifted변수에 이미지저장 (위치가 변경된 이미지) (이미지, 변환행렬, 결과이미지크기)
cv2.imshow("Shifted Down and Right", shifted)                                   #Shifted Down and Right라는 이름으로 shifted이미지 출력

M = np.float32([[1, 0, -50], [0, 1, -90]])                                      #변환행렬 2X3의 float32 type의 numpy array [[1,0,X축 이동],[0,1,Y축 이동]]
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))            #shifted변수에 이미지저장 (위치가 변경된 이미지) (이미지, 변환행렬, 결과이미지크기)
cv2.imshow("Shifted Up and Left", shifted)                                      #Shifted Up and Left라는 이름으로 shifted이미지 출력

#####################################################6.3
shifted = imutils.translate(image, 0, 100)                                      #image를 x축 0만큼, y축 100만큼 이동한 이미지 shifted변수에 저장
cv2.imshow("Shifted Down", shifted)                                             #Shifted Down이라는 이름으로 shifted이미지 출력
cv2.waitKey(0)                                                                  #키 입력이 있을때 까지 대기
