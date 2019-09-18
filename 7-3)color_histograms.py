from __future__ import print_function                                                      #파이썬 2와 3의 버전차이로 인해 생기는 문제방지 및 호환되도록 사용
from matplotlib import pyplot as plt                                                       #matplotlib- 파이썬에서 Matlab과 유사한 그래프 표시를 가능케 하는 라이브러리 / pyplot API - Matlab처럼 커맨드방식 API
import numpy as np                                                                         #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import argparse                                                                            #아규먼트 입력을 위한 argparse
import cv2                                                                                 #Open CV2

ap = argparse.ArgumentParser()                                                             #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")              #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                               #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                                          #args변수의 image에 대응하는 사진경로 불러와서 image 변수에 이미지 저장
cv2.imshow("Original", image)                                                              #Original 이름으로 image이미지 출력
cv2.waitKey(0)                                                                             #키 입력이 있을때 까지 대기

#########################################################################7-4
chans = cv2.split(image)                                                                   #이미지 색채널 분할
colors = ("b", "g", "r")                                                                   #튜플 colors에 ("b", "g", "r") 저장
plt.figure()                                                                               #그래프 그릴 창인 figure생성 / plt.figure(figsize=(9,9))처럼 최초 창의 크기설정도 가능
plt.title("'Flattened' Color Histogram")                                                   #그래프 title 설정
plt.xlabel("Bins")                                                                         #그래프 x축 label 설정
plt.ylabel("# of Pixels")                                                                  #그래프 y축 label 설정

for (chan, color) in zip(chans, colors):                                                   #
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])                                #
    plt.plot(hist, color = color)                                                          #hist값 그래프 그리기 / 각 color별
    plt.xlim([0, 256])                                                                     #x축의 최소값, 최대값 설정
    
########################################################################7-5
fig = plt.figure()                                                                         #그래프 그릴 창인 figure생성 / plt.figure(figsize=(9,9))처럼 최초 창의 크기설정도 가능

ax = fig.add_subplot(131)                                                                  #
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])        #
p = ax.imshow(hist, interpolation = "nearest")                                             #
ax.set_title("2D Color Histogram for G and B")                                             #그래프 title 설정
plt.colorbar(p)                                                                            #

ax = fig.add_subplot(132)                                                                  #
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])        #
p = ax.imshow(hist, interpolation = "nearest")                                             #
ax.set_title("2D Color Histogram for G and R")                                             #그래프 title 설정
plt.colorbar(p)                                                                            #

ax = fig.add_subplot(133)                                                                  #
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])        #
p = ax.imshow(hist, interpolation = "nearest")                                             #
ax.set_title("2D Color Histogram for B and R")                                             #그래프 title 설정
plt.colorbar(p)                                                                            #

print("2D histogram shape: {}, with {} values".format(                                     #
    hist.shape, hist.flatten().shape[0]))

#########################################################################7-6
hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])         #
print("3D histogram shape: {}, with {} values".format(                                     #
    hist.shape, hist.flatten().shape[0]))
plt.show()                                                                                 #생성된 모든 figure 출력
