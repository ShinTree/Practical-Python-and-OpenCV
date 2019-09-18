import numpy as np                                                                   #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import argparse                                                                      #아규먼트 입력을 위한 argparse
import cv2                                                                           #Open CV2

ap = argparse.ArgumentParser()                                                       #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")        #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                         #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                                    #args변수의 image에 대응하는 사진경로 불러와서 image 변수에 이미지 저장
(B, G, R) = cv2.split(image)                                                         #이미지 색채널 분할 -> 각각 하나의 색채널을 갖기때문에 GRAYSCALE로 보임

cv2.imshow("Red", R)                                                                 #Red 이름으로 R이미지 출력
cv2.imshow("Green", G)                                                               #Green 이름으로 G이미지 출력
cv2.imshow("Blue", B)                                                                #Blue 이름으로 B이미지 출력
cv2.waitKey(0)                                                                       #키 입력이 있을때 까지 대기

merged = cv2.merge([B, G, R])                                                        #이미지 색채널 합치기 -> 원본사진
cv2.imshow("Merged", merged)                                                         #Merged이름으로 merged이미지 출력
cv2.waitKey(0)                                                                       #키 입력이 있을때 까지 대기
cv2.destroyAllWindows()                                                              #생성된 모든 윈도우 종료

######################################################################6-23
zeros = np.zeros(image.shape[:2], dtype = "uint8")                                   #image 크기만큼의 행렬 0으로 초기화
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))                                      #Red이름으로 붉은색만 표현한 이미지 출력
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))                                    #Green이름으로 초록색만 표현한 이미지 출력
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))                                     #Blue이름으로 파란색만 표현한 이미지 출력
cv2.waitKey(0)                                                                       #키 입력이 있을때 까지 대기
