from matplotlib import pyplot as plt                                              #matplotlib- 파이썬에서 Matlab과 유사한 그래프 표시를 가능케 하는 라이브러리 / pyplot API - Matlab처럼 커맨드방식 API
import numpy as np                                                                #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import argparse                                                                   #아규먼트 입력을 위한 argparse
import cv2                                                                        #Open CV2

def plot_histogram(image, title, mask = None):                                    #사용자함수 생성
    chans = cv2.split(image)                                                      #이미지 색채널 분할
    colors = ("b", "g", "r")                                                      #튜플 colors에 ("b", "g", "r") 저장
    plt.figure()                                                                  #그래프 그릴 창인 figure생성 / plt.figure(figsize=(9,9))처럼 최초 창의 크기설정도 가능
    plt.title(title)                                                              #그래프 title 설정
    plt.xlabel("Bins")                                                            #그래프 x축 label 설정
    plt.ylabel("# of Pixels")                                                     #그래프 y축 label 설정

    for (chan, color) in zip(chans, colors):                                      #zip() - 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])                   #
        plt.plot(hist, color = color)                                             #hist값 그래프 그리기 / 각 color별
        plt.xlim([0, 256])                                                        #x축의 최소값, 최대값 설정

#########################################################################7-9
ap = argparse.ArgumentParser()                                                    #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")     #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                      #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                                 #args변수의 image에 대응하는 사진경로 불러와서 image 변수에 이미지 저장
cv2.imshow("Original", image)                                                     #Original 이름으로 image이미지 출력
plot_histogram(image, "Histogram for Original Image")                             #image 이미지로 "Histogram for Original Image" 타이틀의 히스토그램 생성
cv2.waitKey(0)                                                                    #키 입력이 있을때 까지 대기

#########################################################################7-10
mask = np.zeros(image.shape[:2], dtype = "uint8")                                 #image크기의 행렬 0으로 초기화
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)                                #사각형 그리기(사각형 그릴 이미지,시작점 좌표,종료점 좌표,색상,선 굵기(-1:채워진도형))
cv2.imshow("Mask", mask)                                                          #Mask 이름으로 mask이미지 출력
cv2.waitKey(0)                                                                    #키 입력이 있을때 까지 대기

masked = cv2.bitwise_and(image, image, mask = mask)                               #mask 이미지의 흰색 좌표 영역만 image출력, 나머지는 검은색 (이미지, 이미지[, 결과파일][, 적용 영역 지정])
cv2.imshow("Applying the Mask", masked)                                           #Applying the Mask 이름으로 masked이미지 출력
cv2.waitKey(0)                                                                    #키 입력이 있을때 까지 대기

#########################################################################7-11
plot_histogram(image, "Histogram for Masked Image", mask = mask)                  #image 이미지에 mask로 마스크처리한 이미지로 "Histogram for Masked Image" 타이틀의 히스토그램 생성
plt.show()                                                                        #생성된 모든 figure 출력
