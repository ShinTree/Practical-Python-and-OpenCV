import numpy as np                                                               #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import argparse                                                                  #아규먼트 입력을 위한 argparse
import imutils                                                                   #resize함수를 쓰기위한 imutils(사용자라이브러리)
import cv2                                                                       #Open CV2

ap = argparse.ArgumentParser()                                                   #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")    #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                     #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                                #args변수의 image에 대응하는 사진경로 불러와서 image 변수에 이미지 저장
cv2.imshow("Original", image)                                                    #Origianl이라는 이름으로 image이미지 출력

r = 150.0 / image.shape[1]                                                       #변수 r에 150/이미지 넓이 저장
dim = (150, int(image.shape[0] * r))                                             #변수 dim에 튜플 (150, 이미지 높이 * r) 저장
                                                                                 #resized변수에 이미지저장 (크기가 변경된 이미지) (이미지, 변경할크기 튜플(가로,세로), 가로사이즈 배수, 세로사이즈 배수,
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)                 #                                                 보간법(사이즈 줄일 때 : cv2.INTER_AREA, 사이즈 키울 때 : cv2.INTER_CUBIC, cv2.INTER_LINEAR))
cv2.imshow("Resized (Width)", resized)                                           #Resized (Width)라는 이름으로 resized이미지 출력
cv2.waitKey(0)                                                                   #키 입력이 있을때 까지 대기

########################################################6-8
r = 50.0 / image.shape[0]                                                        #변수 r에 50/이미지 높이 저장
dim = (int(image.shape[1] * r), 50)                                              #변수 dim에 튜플 (정수(이미지 넓이 * r), 50) 저장
                                                                                 #resized변수에 이미지저장 (크기가 변경된 이미지) (이미지, 변경할크기 튜플(가로,세로), 가로사이즈 배수, 세로사이즈 배수,
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)                 #                                                 보간법(사이즈 줄일 때 : cv2.INTER_AREA, 사이즈 키울 때 : cv2.INTER_CUBIC, cv2.INTER_LINEAR))
cv2.imshow("Resized (Height)", resized)                                          #Resized (Height)라는 이름으로 resized이미지 출력
cv2.waitKey(0)                                                                   #키 입력이 있을때 까지 대기

########################################################6-9
resized = imutils.resize(image, width = 100)                                     #image를 같은 가로세로 비율의 넓이 100크기로 사이즈 변환하여 resized변수에 저장
cv2.imshow("Resized via Function", resized)                                      #Resized via Function이라는 이름으로 resized이미지 출력
cv2.waitKey(0)                                                                   #키 입력이 있을때 까지 대기

########################################################6-10
resized = imutils.resize(image, height = 50)                                     #image를 같은 가로세로 비율의 높이 50크기로 사이즈 변환하여 resized변수에 저장
cv2.imshow("Resized via Function2", resized)                                     #Resized via Function2라는 이름으로 resized이미지 출력
cv2.waitKey(0)                                                                   #키 입력이 있을때 까지 대기
