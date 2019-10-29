# 데이터 그래프로 표현하기
# 그래프를 그리기위한 라이브러리 matplotlib, 이를 기반으로 좀 더 정교한 그래프를 그릴수 있게 도와주는 seaborn 라이브러리 사용

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('C:\\Users\\User\\Documents\\Practical-Python-and-OpenCV\\deeplearning\\dataset\\pima-indians-diabetes.csv',
                 names = ["pregnant", "plasma", "pressure", "thickness", "insulin", "BMI", "pedigree", "age", "class"])

# 그래프의 크기 결정
plt.figure(figsize=(12,12))

# seaborn 라이브러리 중 항목간의 상관관계를 나타내주는 heatmap 함수
# 두 항목씩 짝을 지은 뒤 각각 어떤 패턴으로 변화하는지 관찰하는 함수
# 두 항목이 전혀 다른 패턴으로 변화 -> 0 / 서로 비슷한 패턴으로 변화 -> 1 가까운 값 출력
sns.heatmap(df.corr(), linewidths=0.1, vmax=0.5, cmap=plt.cm.gist_heat, linecolor='white', annot=True)

# 그래프 출력
plt.show()

# plasma와 class 항목만 떼어 두 항목 간의 관계를 그래프로 다시한번 확인
grid = sns.FacetGrid(df, col='class')
grid.map(plt.hist, 'plasma', bins=10)
plt.show()
