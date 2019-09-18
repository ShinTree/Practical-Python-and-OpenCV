import argparse                                                                   #아규먼트 입력을 위한 argparse
import cv2                                                                        #Open CV2

ap = argparse.ArgumentParser()                                                    #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")     #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                      #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                                 #args변수의 image에 대응하는 사진경로 불러와서 image 변수에 이미지 저장
cv2.imshow("Original", image)                                                     #Origianl이라는 이름으로 image이미지 출력

flipped = cv2.flip(image, 1)                                                      #(이미지, 1-좌우반전 / 0-상하반전 / -값 상하좌우반전)
cv2.imshow("Fliipped Horizontally", flipped)                                      #Flipped Horizontally라는 이름으로 flipped이미지 출력

flipped = cv2.flip(image, 0)                                                      #(이미지, 1-좌우반전 / 0-상하반전 / -값 상하좌우반전)
cv2.imshow("Flipped Vertically", flipped)                                         #Flipped Vertically라는 이름으로 flipped이미지 출력

flipped = cv2.flip(image, -1)                                                     #(이미지, 1-좌우반전 / 0-상하반전 / -값 상하좌우반전)
cv2.imshow("Flipped Horizontally & vertically", flipped)                          #Flipped Horizontally & vertically라는 이름으로 flipped이미지 출력
cv2.waitKey(0)                                                                    #키 입력이 있을때 까지 대기
