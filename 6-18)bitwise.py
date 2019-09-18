import numpy as np                                                           #numpy - 벡터, 행렬 연산 지원하는 라이브러리
import cv2                                                                   #Open CV2

rectangle = np.zeros((300, 300), dtype = "uint8")                            #300,300크기의 행렬 0으로 초기화
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)                      #사각형 그리기(이미지, 시작점 좌표, 종료점 좌표, 색상, 선 두께(-1 = 도형채우기))
cv2.imshow("Rectangle", rectangle)                                           #Rectangle이름으로 rectangle 이미지 출력

circle = np.zeros((300, 300), dtype = "uint8")                               #300,300크기의 행렬 0으로 초기화
cv2.circle(circle, (150, 150), 150, 255, -1)                                 #원 그리기(이미지, 중심 좌표, 반지름, 색상, 선 두께(-1 = 도형채우기))
cv2.imshow("Circle", circle)                                                 #Circle이름으로 circle 이미지 출력

################################################################6-19
bitwiseAnd = cv2.bitwise_and(rectangle, circle)                              #두 그림 모두 흰색인 부분만 흰색으로 표현 (이미지, 이미지[, 결과파일][, 적용 영역 지정])
cv2.imshow("AND", bitwiseAnd)                                                #AND이름으로 bitwiseAnd이미지 출력
cv2.waitKey(0)                                                               #키 입력이 있을때 까지 대기

bitwiseOr = cv2.bitwise_or(rectangle, circle)                                #두 그림 둘중 하나라도 흰색인 부분만 흰색으로 표현 (이미지, 이미지[, 결과파일][, 적용 영역 지정])
cv2.imshow("OR", bitwiseOr)                                                  #OR이름으로 bitwiseOr이미지 출력
cv2.waitKey(0)                                                               #키 입력이 있을때 까지 대기

bitwiseXor = cv2.bitwise_xor(rectangle, circle)                              #두 그림에서 값이 같으면 검은색, 다르면 흰색 표현 (이미지, 이미지[, 결과파일][, 적용 영역 지정])
cv2.imshow("XOR", bitwiseXor)                                                #XOR이름으로 bitwiseXor이미지 출력
cv2.waitKey(0)                                                               #키 입력이 있을때 까지 대기

bitwiseNot = cv2.bitwise_not(circle)                                         #색이 반대로 표현 (이미지[, 결과파일][, 적용 영역 지정])
cv2.imshow("NOT", bitwiseNot)                                                #NOT 이름으로 bitwiseNot이미지 출력
cv2.waitKey(0)                                                               #키 입력이 있을때 까지 대기
