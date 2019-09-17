import numpy as np                                                       #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import cv2                                                               #OpenCV

canvas = np.zeros((300, 300, 3), dtype = "uint8")                        #데이터타입 uint8인 (height,width,bpp)크기의 3차원 행렬 canvas생성
                                                                         #bpp(bits per pixel) - 색 요소에 쓰이는 비트의 수
#####################################################5.2
green = (0, 255, 0)                                                      #(b,g,r) (0,255,0) 값 green변수 생성
cv2.line(canvas, (0, 0), (300, 300), green)                              #(선 그릴 이미지,시작점 좌표,종료점 좌표,색상)
cv2.imshow("Canvas", canvas)                                             #Canvas라는 창 이름으로 canvas이미지 출력
cv2.waitKey(0)                                                           #키 입력이 있을때 까지 대기

red = (0, 0, 255)                                                        #(b,g,r) (0,0,255) 값 red변수 생성
cv2.line(canvas, (300, 0), (0, 300), red, 3)                             #(선 그릴 이미지,시작점 좌표,종료점 좌표,색상,선 굵기)
cv2.imshow("Canvas", canvas)                                             #Canvas라는 창 이름으로 canvas이미지 출력
cv2.waitKey(0)                                                           #키 입력이 있을때 까지 대기

#####################################################5.3
cv2.rectangle(canvas, (10, 10), (60, 60), green)                         #(사각형 그릴 이미지,시작점 좌표,종료점 좌표,색상) 
cv2.imshow("Canvas", canvas)                                             #Canvas라는 창 이름으로 canvas이미지 출력
cv2.waitKey(0)                                                           #키 입력이 있을때 까지 대기

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)                     #(사각형 그릴 이미지,시작점 좌표,종료점 좌표,색상,선 굵기) 
cv2.imshow("Canvas", canvas)                                             #Canvas라는 창 이름으로 canvas이미지 출력
cv2.waitKey(0)                                                           #키 입력이 있을때 까지 대기

blue = (255, 0, 0)                                                       #(b,g,r) (255,0,0) 값 blue변수 생성
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)                   #(사각형 그릴 이미지,시작점 좌표,종료점 좌표,색상,선 굵기(-1은 색채워진 도형))
cv2.imshow("Canvas", canvas)                                             #Canvas라는 창 이름으로 canvas이미지 출력
cv2.waitKey(0)                                                           #키 입력이 있을때 까지 대기

#####################################################5.4
canvas = np.zeros((300, 300, 3), dtype = "uint8")                        #데이터타입 uint8인 (height,width,bpp)크기의 3차원 행렬 canvas생성
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)        #canvas.shape = (300,300), //연산자 -> 나누기후 정수의 몫 (정중앙좌표 찾기)
white = (255, 255, 255)                                                  #(b,g,r) (255,255,255) 값 white변수 생성

for r in range(0, 175, 25):                                              #r값 0~174까지 25씩 더해서 출력(0,25,50,75,100,125,150)
    cv2. circle(canvas, (centerX, centerY), r, white)                    #(원 그릴 이미지,원의 중심 좌표,반지름,색상)

cv2.imshow("Canvas", canvas)                                             #Canvas라는 창 이름으로 canvas이미지 출력
cv2.waitKey(0)                                                           #키 입력이 있을때 까지 대기

#####################################################5.5
for i in range(0, 25):                                                   #i값 0~24 1씩 더해서 출력(0,1,2,...,24)
    radius = np.random.randint(5, high = 200)                            #5~199 랜덤값 생성, numpy.random.randint(low(최소),high(최대),size(난수개수))
    color = np.random.randint(0, high = 256, size = (3,)).tolist()       #0~255 랜덤값 3개 array로 생성, list로 변환 
    pt = np.random.randint(0, high = 300, size = (2,))                   #0~299 랜덤값 2개 array로 생성 
    
    cv2.circle(canvas, tuple(pt), radius, color, -1)                     #(원 그릴 이미지,원의 중심 좌표,반지름,색상,선 굵기(-1은 색채워진 도형))

cv2.imshow("Canvas", canvas)                                             #Canvas라는 창 이름으로 canvas이미지 출력
cv2.waitKey(0)                                                           #키 입력이 있을때 까지 대기
