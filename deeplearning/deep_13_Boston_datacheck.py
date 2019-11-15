import pandas as pd

df = pd.read_csv("D:\개발\Practical-Python-and-OpenCV\deeplearning\dataset\housing.csv", delim_whitespace=True, header=None)

print(df.info())
print("\n")
print(df.head())
