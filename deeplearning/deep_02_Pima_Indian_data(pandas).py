# pandas를 활용한 데이터 조사
# 데이터를 다루기위한 라이브러리 pandas활용

import pandas as pd
df = pd.read_csv('C:\\Users\\User\\Documents\\Practical-Python-and-OpenCV\\deeplearning\\dataset\\pima-indians-diabetes.csv',
                 names = ["pregnant", "plasma", "pressure", "thickness", "insulin", "BMI", "pedigree", "age", "class"])

# 데이터의 첫 5줄 출력
print(df.head(5))
print("\n")

# 데이터 항목 별 갯수, 정보의 형식 출력
print(df.info())
print("\n")

# 데이터 정보별 특징 (샘플수, 평균, 표준편차, 최솟값, 백분위 수로 25%, 50%, 75%, 최댓값)
print(df.describe())
print("\n")

# 데이터의 일부 칼럼만 출력
print(df[['pregnant', 'class']])
print("\n")

# 데이터 가공하기 -> 임신횟수와 당뇨병 발병 확률
print(df[['pregnant', 'class']].groupby(['pregnant'], as_index=False).mean().sort_values(by='pregnant', ascending=True))
# groupby함수로 'pregnant' 정보를 기준으로 하는 새그룹을 생성
# as_indes=False는 pregnant 정보 옆 새로운 Index 생성
# mean 함수를 사용해 평균을 구하고, sort_values 함수를 써서 pregnant 칼럼을 오름차순(ascending)으로 정리

