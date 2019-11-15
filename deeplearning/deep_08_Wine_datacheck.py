import pandas as pd

# 데이터 load / 원본 데이터의 몇% 사용할지 지정 (1=100%) 
df_pre = pd.read_csv('D:\\개발\\Practical-Python-and-OpenCV\\deeplearning\\dataset\\wine.csv', header=None)
df = df_pre.sample(frac=1)

# 불러온 데이터의 처음 5줄만 출력
print(df.head(5))

# 전체 정보 출력
print(df.info())
