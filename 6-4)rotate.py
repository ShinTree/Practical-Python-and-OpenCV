import numpy as np                                                              #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import argparse                                                                 #아규먼트 입력을 위한 argparse
import imutils                                                                  #rotate함수를 쓰기위한 imutils(사용자라이브러리)
import cv2                                                                      #Open CV2

ap = argparse.ArgumentParser()                                                  #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")   #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                    #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                               #args변수의 image에 대응하는 사진경로 불러와서 image 변수에 이미지 저장
cv2.imshow("Original", image)                                                   #Origianl이라는 이름으로 image이미지 출력

(h, w) = image.shape[:2]                                                        #h-이미지의 높이, w-이미지의 넓이
center = (w // 2, h // 2)                                                       #이미지의 중심값 center변수에 저장

M = cv2.getRotationMatrix2D(center, 45, 1.0)                                    #변환행렬 생성(이미지의 중심좌표, 회전 각도(+는 시계방향), scale factor)
rotated = cv2.warpAffine(image, M, (w, h))                                      #rotated변수에 이미지저장 (위치가 변경된 이미지) (이미지, 변환행렬, 결과이미지크기)
cv2.imshow("Rotated by 45 Degrees", rotated)                                    #Rotated by 45 Degrees라는 이름으로 rotated이미지 출력

M = cv2.getRotationMatrix2D(center, -90, 1.0)                                   #변환행렬 생성(이미지의 중심좌표, 회전 각도(-는 반시계방향), scale factor)
rotated = cv2.warpAffine(image, M, (w, h))                                      #rotated변수에 이미지저장 (위치가 변경된 이미지) (이미지, 변환행렬, 결과이미지크기)
cv2.imshow("Rotated by -90 Degrees", rotated)                                   #Rotated by -90 Degrees라는 이름으로 rotated이미지 출력
cv2.waitKey(0)                                                                  #키 입력이 있을때 까지 대기

######################################################6-6
rotated = imutils.rotate(image, 180)                                            #image를 180도 회전한 이미지 rotated변수에 저장
cv2.imshow("Rotated by 180 Degrees", rotated)                                   #Rotated by 180 Degrees라는 이름으로 rotated이미지 출력
cv2.waitKey(0)                                                                  #키 입력이 있을때 까지 대기
