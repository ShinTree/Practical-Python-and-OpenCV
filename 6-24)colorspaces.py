import numpy as np                                                               #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import argparse                                                                  #아규먼트 입력을 위한 argparse
import cv2                                                                       #Open CV2

ap = argparse.ArgumentParser()                                                   #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")    #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                     #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                                #args변수의 image에 대응하는 사진경로 불러와서 image 변수에 이미지 저장
cv2.imshow("Original", image)                                                    #Original 이름으로 image이미지 출력

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                   #BGR이미지 GRAYSCALE이미지로 변환
cv2.imshow("Gray", gray)                                                         #Gray 이름으로 gray이미지 출력

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)                                     #BGR이미지 HSV이미지로 변환
cv2.imshow("HSV", hsv)                                                           #HSV 이름으로 hsv이미지 출력

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)                                     #BGR이미지 LAB이미지로 변환
cv2.imshow("L*a*b*", lab)                                                        #L*a*b* 이름으로 lab이미지 출력
cv2.waitKey(0)                                                                   #키 입력이 있을때 까지 대기
