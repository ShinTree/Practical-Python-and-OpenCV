from __future__ import print_function                                                    #파이썬 2와 3의 버전차이로 인해 생기는 문제방지 및 호환되도록 사용
import argparse                                                                          #아규먼트 입력을 위한 argparse 임포트
import cv2                                                                               #Open CV2 임포트

ap = argparse.ArgumentParser()                                                           #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")            #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                             #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                                        #"image"파일 이미지 image로 저장
cv2.imshow("Original", image)                                                            #Original이라는 창 이름으로 image이미지 출력

###########################################################4.2
(b,g,r) = image[0,0]                                                                     #(b,g,r) 튜플에 image 픽셀 0,0의 색상값(b,g,r)대입
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))                  #(r,g,b) 순서로 출력 (포메팅)

image[0, 0] = (0, 0, 255)                                                                #image이미지의 y=0, x=0위치의 픽셀 (b,g,r) (0,0,255) 색으로 변환
(b, g, r) = image[0, 0]                                                                  #(b,g,r) 튜플에 image 픽셀 0,0의 색상값(b,g,r)대입
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))                  #(r,g,b) 순서로 출력 (포메팅)
cv2.imshow("Check", image)                                                               #Check라는 창 이름으로 image이미지 출력

##########################################################4.3
corner = image[0:100, 0:100]                                                             #image이미지의 y,x 0~100픽셀 잘라서 corner이미지 생성
cv2.imshow("Corner", corner)                                                             #Corner라는 창 이름으로 corner이미지 출력

image[0:100, 0:100] = (0, 255, 0)                                                        #image이미지의 y,x 0~100픽셀 (b,g,r) (0,255,0) 색으로 변환

cv2.imshow("Updated", image)                                                             #Updated라는 창 이름으로 image이미지 출력
cv2.waitKey(0)                                                                           #키 입력이 있을때 까지 대기

##########################################################4.4

