import numpy as np                                                                 #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import argparse                                                                    #아규먼트 입력을 위한 argparse
import cv2                                                                         #Open CV2

ap = argparse.ArgumentParser()                                                     #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")      #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                       #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                                  #args변수의 image에 대응하는 사진경로 불러와서 image 변수에 이미지 저장
cv2.imshow("Original", image)                                                      #Origianl 이름으로 image이미지 출력

mask = np.zeros(image.shape[:2], dtype = "uint8")                                  #image 크기만큼의 행렬 0으로 초기화 
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)                              #image의 중심좌표 (cX, cY) 저장
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)               #사각형 그리기(이미지, 시작점 좌표, 종료점 좌표, 색상, 선 두께(-1 = 도형채우기))
cv2.imshow("Mask", mask)                                                           #Mask 이름으로 mask이미지 출력

masked = cv2.bitwise_and(image, image, mask = mask)                                #mask 이미지의 흰색 좌표 영역만 image출력, 나머지는 검은색 (이미지, 이미지[, 결과파일][, 적용 영역 지정])
cv2.imshow("Mask Applied to Image", masked)                                        #Mask Applied to Image 이름으로 masked이미지 출력
cv2.waitKey(0)                                                                     #키 입력이 있을때 까지 대기

############################################################6-21
mask = np.zeros(image.shape[:2], dtype = "uint8")                                  #image 크기만큼의 행렬 0으로 초기화
cv2.circle(mask, (cX, cY), 100, 255, -1)                                           #원 그리기(이미지, 중심 좌표, 반지름, 색상, 선 두께(-1 = 도형채우기))
masked = cv2.bitwise_and(image, image, mask = mask)                                #mask 이미지의 흰색 좌표 영역만 image출력, 나머지는 검은색 (이미지, 이미지[, 결과파일][, 적용 영역 지정])
cv2.imshow("Mask", mask)                                                           #Mask 이름으로 mask이미지 출력
cv2.imshow("Mask Applied to Image", masked)                                        #Mask Applied to Image 이름으로 masked이미지 출력
cv2.waitKey(0)                                                                     #키 입력이 있을때 까지 대기
