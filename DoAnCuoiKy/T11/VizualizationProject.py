import numpy as np
import pandas as pd

# Import file csv vào
data = pd.read_csv("D:/DataVizualization/Netflix.csv")

#Chuyển data vào thành dataframe
df = pd.DataFrame(data)

#In ra dataframe nhưng các ô có dữ liệu NA sẽ là mang giá trị True và ngược lại thì mang giá trị False
print(df.isna())

#Loại bỏ giá trị na
df1 = df.dropna()
#Kiểm tra lại
print(df1.isna())

# Xuất file đã xử lý thành tệp csv
df1.to_csv("D:/DataVizualization/NetflixTitle.csv")