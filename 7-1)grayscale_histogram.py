from matplotlib import pyplot as plt                                            #matplotlib- 파이썬에서 Matlab과 유사한 그래프 표시를 가능케 하는 라이브러리 / pyplot API - Matlab처럼 커맨드방식 API
import argparse                                                                 #아규먼트 입력을 위한 argparse
import cv2                                                                      #Open CV2

ap = argparse.ArgumentParser()                                                  #아규먼트 받기위한 ap생성
ap.add_argument("-i", "--image", required = True, help = "Path to the image")   #입력 받으려는 인자의 조건 설정 ("호출 명령어", required(필수입력사항인가?), default(디폴트값), help(힌트))
args = vars(ap.parse_args())                                                    #딕셔너리 {'image' : '사진경로'} args변수에 저장

image = cv2.imread(args["image"])                                               #args변수의 image에 대응하는 사진경로 불러와서 image 변수에 이미지 저장

###################################################################7-2
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                 #BGR이미지 GRAYSCALE이미지로 변환
cv2.imshow("Original", image)                                                   #Original 이름으로 image이미지 출력

hist = cv2.calcHist([image], [0], None, [256], [0, 256])                        #이미지 히스토그램을 찾기위한 함수 ([이미지], Grayscale은 [0]/컬러는 BGR에 각각 [0].[1].[2]인자 입력, mask(전체시 None), [BIN개수], 픽셀값 범위(보통 [0, 256]))

plt.figure()                                                                    #그래프 그릴 창인 figure생성 / plt.figure(figsize=(9,9))처럼 최초 창의 크기설정도 가능
plt.title("Grayscale Histogram")                                                #그래프 title 설정
plt.xlabel("Bins")                                                              #그래프 x축 label 설정
plt.ylabel("# of Pixels")                                                       #그래프 y축 label 설정
plt.plot(hist)                                                                  #hist값 그래프 그리기
plt.xlim([0, 256])                                                              #x축의 최소값, 최대값 설정
plt.show()                                                                      #생성된 모든 figure 출력
cv2.waitKey(0)                                                                  #키 입력이 있을때 까지 대기

