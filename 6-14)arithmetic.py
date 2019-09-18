from __future__ import print_function                                             #파이썬 2와 3의 버전차이로 인해 생기는 문제방지 및 호환되도록 사용
import numpy as np                                                                #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import argparse                                                                   #아규먼트 입력을 위한 argparse
import cv2                                                                        #Open CV2

ap = argparse.ArgumentParser()                                                    #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")     #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                      #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                                 #args변수의 image에 대응하는 사진경로 불러와서 image 변수에 이미지 저장
cv2.imshow("Original", image)                                                     #Origianl이라는 이름으로 image이미지 출력

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))         #
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))       #

print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))                #
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))                 #

cv2.waitKey(0)                                                                    #키 입력이 있을때 까지 대기

####################################################################6-17
M = np.ones(image.shape, dtype = "uint8") * 100                                   #
added = cv2.add(image, M)                                                         #
cv2.imshow("Added", added)                                                        #Added라는 이름으로 added이미지 출력

M = np.ones(image.shape, dtype = "uint8") * 50                                    #
subtracted = cv2.subtract(image, M)                                               #
cv2.imshow("Subtracted", subtracted)                                              #Substracted라는 이름으로 subtracted이미지 출력
cv2.waitKey(0)                                                                    #키 입력이 있을때 까지 대기
